from PyQt5.QtWidgets import QDialog, QFileDialog

import py_ui.create_account
import py_ui.login_account
from config import *
from exceptions import *
from service import *
from validators import *


class LoginAccountApp(QDialog, py_ui.login_account.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_login.clicked.connect(self.__login)
        self.lbl_create_account.clicked.connect(self.__create_account)

    def __get_email(self):
        email = self.edit_email.text()
        return email

    def __get_password(self):
        password = self.edit_password.text()
        return hash_data(password)

    def __is_fields_empty(self):
        fields = [self.edit_email, self.edit_password]

        for field in fields:
            if not field.text():
                return True
        else:
            return False

    def __show_error(self, text):
        self.lbl_info.setText(str(text))
        self.lbl_info.adjustSize()

    def __get_login_data(self) -> dict:
        return {
            'email': self.__get_email(),
            'password': self.__get_password()
        }

    def __login(self):
        try:
            if self.__is_fields_empty():
                raise FormFillingError(get_filing_error_text('empty_fields'))

            data = self.__get_login_data()
            is_login_exists = check_login_exists(data)
            is_login_data_correct = check_login_data_correctness(data)

            if not is_login_exists:
                raise FormFillingError(get_filing_error_text('login_not_exists'))
            if not is_login_data_correct:
                raise FormFillingError(get_filing_error_text('incorrect_login_data'))
            else:
                save_current_user_to_local(data)
                self.close()
        except FormFillingError as e:
            self.__show_error(e)

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
        self.btn_add_photo.clicked.connect(self.__choose_photo)

    def __get_password(self):
        password = self.edit_password.text()
        password_again = self.edit_password_again.text()

        if not password == password_again:
            raise FormFillingError(get_filing_error_text('passwords_not_equal'))

        if not PasswordValidator(password).validate():
            raise FormFillingError(get_filing_error_text('invalid_password'))

        return hash_data(password)

    def __get_birthday(self):
        date = self.dtchoice_birthday.dateTime().toPyDateTime().timestamp()
        if not DateValidator(date).validate():
            raise FormFillingError(get_filing_error_text('invalid_birthday'))

        return int(date)

    def __get_name(self):
        name = self.edit_name.text()

        for letter in name:
            # If digits in name
            if letter.isdigit():
                raise FormFillingError(get_filing_error_text('invalid_name'))

        return name

    def __get_surname(self):
        surname = self.edit_surname.text()

        for letter in surname:
            # If digits in surname
            if letter.isdigit():
                raise FormFillingError(get_filing_error_text('invalid_name'))

        return surname

    def __get_email(self):
        email = self.edit_email.text()

        if not EmailValidator(email).validate():
            raise FormFillingError(get_filing_error_text('invalid_email'))

        return email
    
    def __is_fields_empty(self) -> bool:
        fields = [self.edit_name, self.edit_surname, self.edit_password]

        for field in fields:
            if not field.text():
                return True
        else:
            return False

    def __choose_photo(self):
        file_name = QFileDialog.getOpenFileName(self, 'Выбрать фотографию', '',
                                                'Картинка (*.jpg, *.png);;Все файлы (*)')[0]

        if not file_name:
            self.avatar_photo = DEFAULT_AVATAR_PATH
            self.btn_add_photo.setText('Добавить фотографию')
            return

        self.avatar_photo = file_name
        self.btn_add_photo.setText(file_name)

    def __show_error(self, text):
        self.lbl_error.setText(str(text))

    def __get_account_data(self):
        return {
            'name': self.__get_name(),
            'surname': self.__get_surname(),
            'email': self.__get_email(),
            'birthday': self.__get_birthday(),
            'gender': self.cmb_gender.currentText()[0],  # First gender symbol
            'password': self.__get_password(),
            'portfolio_count': 0,
            'avatar_photo': self.avatar_photo,
            'post': self.cmb_post.currentText()
        }

    def __create_account(self):
        try:
            # Check empty fields
            if self.__is_fields_empty():
                raise FormFillingError(get_filing_error_text('empty_fields'))

            data = self.__get_account_data()
            self.__show_error('')

            account_is_created = create_account(data)

            # If user was created
            if not account_is_created:
                raise FormFillingError(get_filing_error_text('user_was_created'))

            self.close()
        except FormFillingError as e:
            self.__show_error(e)

    def __login(self):
        login_app = LoginAccountApp()
        self.close()
        login_app.exec_()
