import sys

from PyQt5.QtWidgets import QApplication, QWidget
from py_ui.create_account import Ui_Form

from utils import *
from exceptions import *
from validators import *
from service import *


class CreateAccountApp(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fillUi()

        self.btn_create_account.clicked.connect(self.__create_account)

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

        if not password == password_again:
            raise FormFillingError('Пароли не совпадают')

        if not PasswordValidator(password).validate():
            raise FormFillingError('Пароль не соответствует требованиям')

        return hash_data(password)

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

        return name

    def get_surname(self):
        surname = self.edit_surname.text()

        for letter in surname:
            # If digits in surname
            if letter.isdigit():
                raise FormFillingError('В фамилии не должно быть цифр!')
        
        return surname

    def get_email(self):
        email = self.edit_email.text()

        if not EmailValidator(email).validate():
            raise FormFillingError('Почтовый аддрес не корректный!')

        return hash_data(email)


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
        data['email'] = self.get_email()
        data['birthday'] = self.get_birthday()
        data['post'] = self.cmb_post.currentText()
        # First symbol from gender
        data['gender'] = self.cmb_gender.currentText()[0]
        data['password'] = self.get_password()
        data['portfolio_count'] = 0

        return data

    def __create_account(self):
        try:
            # Check empty fields
            self.check_empty_fields()
            # Get registration data
            data = self.get_grouped_data()
            # Clean error label
            self.show_error('')

            res = create_account(data)

            # If user was created
            if res:
                self.show_error('Пользователь с такой почтой уже создан')

        except FormFillingError as e:
            self.show_error(e)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app_ = CreateAccountApp()
    app_.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
