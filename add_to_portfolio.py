import sys
import datetime

from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox
from py_ui.add_to_portfolio import Ui_Form

from service import *


class AddToPortfolio(QDialog, Ui_Form):
    def __init__(self):
        super().__init__()
        self.portfolio_photo = None

        self.setupUi(self)

        self.btn_add_photo.clicked.connect(self.add_photo)
        self.btn_add_to_portfolio.clicked.connect(self.add_to_portfolio)

    def add_to_portfolio(self):
        competitions_name = self.get_competitions_name()
        place = self.get_place()
        date = self.get_date()
        photo = self.get_photo()

        if not competitions_name:
            self.show_error('Не выбрано название соревнований')
            return

        if not photo:
            self.show_error('Не выбрана фотография')
            return

        res = add_to_portfolio(competitions_name, place, date, photo)
        
        if res:
            msg_box = QMessageBox()
            user_ans = msg_box.information(self, 'Успешно!', 'Информация успешно добавлена в портфолио!')
            
            if user_ans == QMessageBox.Ok:
                self.close()

    def show_error(self, error):
        self.lbl_error.setText(error)
        self.lbl_error.adjustSize()

    def add_photo(self):
        file_name = QFileDialog.getOpenFileName(self, 'Выбрать фотографию', '',
                                                'Картинка (*.jpg, *.png);;Все файлы (*)')[0]

        self.portfolio_photo = file_name
        if file_name:
            self.btn_add_photo.setText('Selected: ' + file_name)
        else:
            self.btn_add_photo.setText('Добавить фотографию')

    def get_competitions_name(self):
        return self.edit_competitions_name.text()

    def get_place(self):
        return self.cmb_place.currentText()

    def get_date(self):
        date = self.edit_date.date().toPyDate()
        datetime_ = datetime.datetime.combine(date, datetime.time(0, 0, 0))
        datetime_timestamp = datetime_.timestamp()

        return int(datetime_timestamp)

    def get_photo(self):
        return self.portfolio_photo


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app_ = AddToPortfolio()
    app_.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
