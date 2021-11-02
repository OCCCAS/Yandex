from PyQt5.QtWidgets import QWidget

from py_ui import app_teacher, app_children


class ChildrenApp(QWidget, app_children.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class TeacherApp(QWidget, app_teacher.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
