from profile import ChildrenProfile, TeacherProfile
from tasks import *
from service import *
from PyQt5.QtWidgets import QApplication
from create_and_login_account import CreateAccountApp


class ChildrenApp(ChildrenProfile, Tasks, QWidget):
    def __init__(self):
        super().__init__()


class TeacherApp(TeacherProfile, ManageTasks, QWidget):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # If account is creating
    crt_acc = False

    # If user not logged in in local, start creating account or logging to account
    if not is_user_logged_in_local():
        create_account_app_ = CreateAccountApp()
        crt_acc = create_account_app_.exec_()

    if not crt_acc and is_user_logged_in_local():
        post = get_user_post_id()
        App = None

        # 1 - teacher, 2 - children
        if post == 1:
            App = TeacherApp
        elif post == 2:
            App = ChildrenApp

        if App:
            app_ = App()
            app_.show()

        sys.excepthook = except_hook
        sys.exit(app.exec())
