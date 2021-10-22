import sys

from PyQt5.QtWidgets import QApplication, QWidget
from py_ui.create_account import Ui_Form

from utils import *
from exceptions import *
from validators import *


class App(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fillUi()

        self.btn_create_account.clicked.connect(self.create_account)

    def fillUi(self):
        self.fill_gender_cmb()
        self.fill_post_cmb()

    def fill_gender_cmb(self):
        choices = ['Мальчик', 'Девочка']
        self.cmb_gender.addItems(choices)

    def fill_post_cmb(self):
        choices = ['Ребенок', 'Воспитатель']
        self.cmb_post.addItems(choices)

    def get_password(self):
        password = self.edit_password.text()
        password_again = self.edit_password_again.text()

        if not PasswordValidator(password).validate():
            raise FormFillingError('Пароль не соответствует требованиям')

        return hash_password(password)

    def get_birthday(self):
        date = self.dtchoice_birthday.dateTime().toPyDateTime().timestamp()
        if not DateValidator(date).validate():
            raise FormFillingError('Дата рождения не корректна!')

        return int(date)

    def get_name(self):
        name = self.edit_name.text()

        for letter in name:
            # If digits in name
            if letter.isdigit():
                raise FormFillingError('В имени не должно быть цифр!')

    def get_surname(self):
        surname = self.edit_surname.text()

        for letter in surname:
            # If digits in surname
            if letter.isdigit():
                raise FormFillingError('В фамилии не должно быть цифр!')

    def get_nick(self):
        nick = self.edit_nick.text()

        # If only nums in nick
        if nick.isdigit():
            raise FormFillingError('В псевдоними должны быть буквы!')

    def check_empty_fields(self):
        fields = [
            self.edit_name,
            self.edit_surname,
            self.edit_password
        ]

        for field in fields:
            if field.text() == '':
                raise FormFillingError('Не все поля заполнены!')

    def show_error(self, text):
        self.lbl_error.setText(str(text))

    def get_grouped_data(self):
        data = {}

        data['name'] = self.get_name()
        data['surname'] = self.get_surname()
        data['nick'] = self.get_nick()
        data['birthday'] = self.get_birthday()
        data['post'] = self.cmb_post.currentText()
        # First symbol from gender
        data['gender'] = self.cmb_gender.currentText()[0]
        data['password'] = self.get_password()

        return data

    def create_account(self):
        try:
            # Check empty fields
            self.check_empty_fields()
            # Get registration data
            data = self.get_grouped_data()
            # Clean error label
            self.show_error('')
            print(data)
        except FormFillingError as e:
            self.show_error(e)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app_ = App()
    app_.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
