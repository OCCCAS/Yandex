import datetime
import sys
import glob

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QTextBrowser 
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from py_ui.profile import Ui_Form

from service import *
from config import *
from add_to_portfolio import AddToPortfolio
from create_and_login_account import CreateAccountApp


class Profile(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fill_profile_info()
        self.fill_portfolio_feed()

        self.btn_add_img_to_portfolio.clicked.connect(self.add_el_to_portfolio)

    def add_el_to_portfolio(self):
        add_to_portfolio_app = AddToPortfolio()
        opened = add_to_portfolio_app.exec_()

        if not opened:
            self.fill_portfolio_feed()

    def clear_portfolio_feed(self):
        layout = self.feed_portfolio.widget().setParent(None)

    def fill_portfolio_feed(self):
        if self.feed_portfolio.widget().layout():
            self.clear_portfolio_feed()

        images = QWidget()
        images_layout = QVBoxLayout()
        user_portfolio_data = get_user_portfolio()

        for portfolio_data in user_portfolio_data:
            file_name = portfolio_data[-1]
            competitions_name = portfolio_data[1]
            date = datetime.datetime.fromtimestamp(portfolio_data[3]).strftime('%d.%m.%Y')
            place = portfolio_data[2]
            
            lbl = QLabel()
            pixmap = QPixmap(file_name)
            pixmap = pixmap.scaledToWidth(images.width() // 2)
            lbl.setAlignment(Qt.AlignCenter)
            lbl.setPixmap(pixmap)

            portfolio_title = QTextBrowser()
            portfolio_title.setText(f'<h2 align="center">{competitions_name}</h2>')
            portfolio_title.setStyleSheet('background-color: rgba(0, 0, 0, 0);')

            portfolio_info = QTextBrowser()
            portfolio_info.setText(f'<h3>Дата: {date}<br>Место: {place}</h3>')
            portfolio_info.setStyleSheet('background-color: rgba(0, 0, 0, 0);')

            images_layout.addWidget(portfolio_title)
            images_layout.addWidget(lbl)
            images_layout.addSpacing(5)
            images_layout.addWidget(portfolio_info)
            images_layout.addSpacing(20)

        images.setLayout(images_layout)

        self.feed_portfolio.setWidget(images)

    @staticmethod
    def get_profile_info():
        user_email = get_current_user_email()

        name = get_user_data(user_email, 'name')
        surname = get_user_data(user_email, 'surname')
        birthday_timestamp = get_user_data(user_email, 'birthday')
        birthday = datetime.datetime.fromtimestamp(birthday_timestamp)
        age = (datetime.datetime.now() - birthday).days // 365
        
        return {'name': f'{name} {surname}', 'age': age}

    def set_profile_photo(self):
        self.lbl_profile_image.setPixmap(QPixmap(get_user_avatar_photo()))

    def fill_profile_info(self):
        profile_info = self.get_profile_info()
        self.lbl_name.setText(profile_info.get('name'))
        self.lbl_age.setText(str(profile_info.get('age')) + ' лет')
        self.set_profile_photo()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    crt_acc = False

    if not is_user_loggined():
        create_account_app_ = CreateAccountApp()
        crt_acc = create_account_app_.exec_()

    if not crt_acc and is_user_loggined():
        app_ = Profile()
        app_.show()

        sys.excepthook = except_hook
        sys.exit(app.exec())

