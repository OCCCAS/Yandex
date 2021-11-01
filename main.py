import sys

from PyQt5.QtWidgets import QApplication

from service import *


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # If account is creating
    crt_acc = False

    start_login_if_needs()

    if not crt_acc and is_user_logged_in_local():
        exit_code = start_main_app_with_post_verification()
        if exit_code:
            sys.excepthook = except_hook
            sys.exit(app.exec())
        else:
            print('ERROR: invalid post id')
