from PyQt5.QtWidgets import QDialog, QFileDialog
import py_ui.create_account
import py_ui.login_account

from utils import *
from exceptions import *
from validators import *
from service import *
from config import *


class LoginAccountApp(QDialog, py_ui.login_account.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_login.clicked.connect(self.__login)
        self.lbl_create_account.clicked.connect(self.__create_account)

    def get_email(self):
        email = self.edit_email.text()
        return email

    def get_password(self):
        password = self.edit_password.text()
        return hash_data(password)

    def is_fields_empty(self):
        fields = [self.edit_email, self.edit_password]

        for field in fields:
            if not field.text():
                return True

        return False

    def show_info(self, text):
        self.lbl_info.setText(text)
        self.lbl_info.adjustSize()

    def __login(self):
        if self.is_fields_empty():
            self.show_info('Не все поля заполнены')
        else:
            self.show_info('')

            data = {
                'email': self.get_email(),
                'password': self.get_password()
            }
            res = login(data)

            if not res:
                self.show_info('Не правильно введен логин или пароль')
            else:
                save_current_user(data)
                self.close()

    def __create_account(self):
        create_account_app = CreateAccountApp()
        self.close()
        create_account_app.exec_()


class CreateAccountApp(QDialog, py_ui.create_account.Ui_Form):
    def __init__(self):
        super().__init__()
        self.avatar_photo = DEFAULT_AVATAR_PATH

        self.setupUi(self)

        self.btn_create_account.clicked.connect(self.__create_account)
        self.lbl_login.clicked.connect(self.__login)
        self.btn_add_photo.clicked.connect(self.choose_photo)

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

        return email

    def check_empty_fields(self):
        fields = [
            self.edit_name,
            self.edit_surname,
            self.edit_password
        ]

        for field in fields:
            if field.text() == '':
                raise FormFillingError('Не все поля заполнены!')

    def choose_photo(self):
        file_name = QFileDialog.getOpenFileName(self, 'Выбрать фотографию', '',
                                                'Картинка jpg (*.jpg);;Картинка png (*.png);;Все файлы (*)')[0]

        if not file_name:
            self.avatar_photo = DEFAULT_AVATAR_PATH
            self.btn_add_photo.setText('Добавить фотографию')
            return

        self.avatar_photo = file_name
        self.btn_add_photo.setText(file_name)

    def show_error(self, text):
        self.lbl_error.setText(str(text))

    def get_grouped_data(self):
        data = {
            'name': self.get_name(),
            'surname': self.get_surname(),
            'email': self.get_email(),
            'birthday': self.get_birthday(),
            'gender': self.cmb_gender.currentText()[0],  # First gender symbol
            'password': self.get_password(),
            'portfolio_count': 0,
            'avatar_photo': self.avatar_photo
        }

        return data

    def __create_account(self):
        try:
            # Check empty fields
            self.check_empty_fields()
            # Get registration data
            data = self.get_grouped_data()
            # Clean error label
            self.show_error('')

            created = create_account(data)

            # If user was created
            if not created:
                self.show_error('Пользователь с такой почтой уже создан')
                return

            save_current_user(data)
            self.close()
        except FormFillingError as e:
            self.show_error(e)

    def __login(self):
        login_app = LoginAccountApp()
        self.close()
        login_app.exec_()
