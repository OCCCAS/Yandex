import sys
import shutil
import pathlib
import glob

from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
from py_ui.profile import Ui_Form

from service import *
from config import *


class Profile(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fill_profile_info()
        self.show_portfolio()

        self.btn_add_img_to_portfolio.clicked.connect(self.add_el_to_portfolio)

    def add_el_to_portfolio(self):
        user_email = get_current_user_email()

        abs_file_name = QFileDialog.getOpenFileName(
            self, 'Выбрать картинку', '',
            'Картинка (*.jpg);;Картинка (*.png);;Все файлы (*)')[0]

        portfolio_index = get_user_data(user_email, 'portfolio_count')
        if not portfolio_index:
            portfolio_index = 0

        new_file_name = f'{user_email}_{portfolio_index}.png'
        database_handler_.execute('UPDATE users SET portfolio_count=portfolio_count + 1 WHERE email=?', (user_email,),
                                  commit=True)

        shutil.copyfile(abs_file_name, os.path.join(PORTFOLIO_PATH, new_file_name))
        self.show_portfolio()

    def clear_portfolio_view(self):
        layout = self.feed_portfolio.widget().setParent(None)

    def show_portfolio(self):
        user_email = get_current_user_email()

        if self.feed_portfolio.widget().layout():
            self.clear_portfolio_view()

        images = QWidget()
        images_layout = QVBoxLayout()

        user_portfolio_files = [file_name for file_name in
                                glob.glob(os.path.join(PORTFOLIO_PATH, f'{user_email}_*.png'))]

        for file_name in user_portfolio_files:
            lbl = QLabel()
            pixmap = QPixmap(file_name)
            pixmap = pixmap.scaledToWidth(self.feed_portfolio.width() - 40)
            lbl.setPixmap(pixmap)
            images_layout.addWidget(lbl)

        images.setLayout(images_layout)

        self.feed_portfolio.setWidget(images)

    def get_profile_info(self):
        user_email = get_current_user_email()

        name = get_user_data(user_email, 'name')
        surname = get_user_data(user_email, 'surname')
        birthday = datetime.datetime.fromtimestamp(get_user_data(user_email, 'birthday')).strftime('%d.%m.%Y')
        post = database_handler_.execute('SELECT posts.name FROM users, posts WHERE'
                                         ' posts.id = users.post AND users.email=?', (user_email,))[0][0]

        text = f'<h3>{name} {surname}:</h3>' \
               f'<ul><li>День рождения: {birthday}</li>' \
               f'<li>Должность: {post}</li></ul>'

        return text

    def fill_profile_info(self):
        text = self.get_profile_info()
        self.tb_profile_info.setText(str(text))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app_ = Profile()
    app_.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
