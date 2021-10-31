import sys

from PyQt5.QtWidgets import QApplication, QWidget


class Example1(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        print(1)


class Example2(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        print(2)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    post = 1
    if post == 1:
        from example1 import Ui_Form
        App = Example1
    elif post == 2:
        from example2 import Ui_Form
        App = Example2
    
    App.__bases__ = App.__bases__ + (Ui_Form, )

    app_ = App()
    app_.show()

    sys.excepthook = except_hook
    sys.exit(app.exec())
