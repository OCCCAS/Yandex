import sys

from PyQt5.QtWidgets import QApplication, QDialog
from py_ui.login_account import Ui_Form

from service import *
from utils import *


class LoginAccountApp(QDialog, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_login.clicked.connect(self.__login)

    def get_email(self):
        email = self.edit_email.text()
        return hash_data(email)

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
                self.show_info('')
                save_current_user(data)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app_ = LoginAccountApp()
    app_.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
