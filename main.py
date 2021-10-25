import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from py_ui.main import Ui_MainWindow


class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fill_table()

    def fill_table(self):
        pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app_ = App()
    app_.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
