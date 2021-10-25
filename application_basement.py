import sys

from PyQt5.QtWidgets import QApplication, QWidget
from ui import Ui_Form


class App(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app_ = App()
    app_.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
