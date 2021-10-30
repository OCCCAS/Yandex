import datetime
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QTextBrowser, QScrollArea
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from py_ui.profile import Ui_Form

from service import *
from add_to_portfolio import AddToPortfolio
from edit_profile import EditProfile
from create_and_login_account import CreateAccountApp
from qportfoliofeed import *


class Profile(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fill_profile_info()
        self.fill_portfolio_feed()

        self.btn_add_img_to_portfolio.clicked.connect(self.__add_to_portfolio)
        self.btn_edit_profile.clicked.connect(self.__edit_profile)

    def __edit_profile(self) -> None:
        edit_profile_app = EditProfile()
        opened = edit_profile_app.exec_()

        if not opened:
            self.fill_profile_info()
            self.set_profile_photo()

    def __add_to_portfolio(self) -> None:
        add_to_portfolio_app = AddToPortfolio()
        opened = add_to_portfolio_app.exec_()

        if not opened:
            self.fill_portfolio_feed()
            self.set_profile_photo()

    def clear_portfolio_feed(self) -> None:
        # self.feed_portfolio has widget which has items and if we remove that widget we remove all portfolio items
        self.feed_portfolio.widget().setParent(None)

    def fill_portfolio_feed(self):
        if self.feed_portfolio.widget().layout():
            self.feed_portfolio.clear_and_emit()

        user_portfolio_data = get_user_portfolio()

        for portfolio_data in user_portfolio_data:
            competitions_name = portfolio_data[1]
            place = portfolio_data[2]
            date = portfolio_data[3]
            file_name = portfolio_data[-1]

            portfolio_item = PortfolioItem(competitions_name, file_name, date, place)
            feed_item = PortfolioFeedItem(portfolio_item)
            self.feed_portfolio.add_item(feed_item)

        self.feed_portfolio.create()

    @staticmethod
    def get_profile_info() -> dict:
        user_email = get_local_user_email()

        name, surname, birthday_timestamp = get_user_data_by_columns(
            ['name', 'surname', 'birthday'],
            user_email
        )
        birthday_datetime = datetime.datetime.fromtimestamp(birthday_timestamp)
        # Now datetime minus birthday datetime, then get days and divide it to days count in year
        age = (datetime.datetime.now() - birthday_datetime).days // 365

        return {'name': f'{name} {surname}', 'age': age}

    def set_profile_photo(self) -> None:
        self.lbl_profile_image.setPixmap(QPixmap(get_user_avatar_photo()))

    def fill_profile_info(self) -> None:
        profile_info = self.get_profile_info()
        self.lbl_name.setText(profile_info.get('name'))
        self.lbl_name.adjustSize()
        self.lbl_age.setText(str(profile_info.get('age')) + ' лет')
        self.set_profile_photo()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    crt_acc = False

    if not is_user_logged_in_local():
        create_account_app_ = CreateAccountApp()
        crt_acc = create_account_app_.exec_()

    if not crt_acc and is_user_logged_in_local():
        app_ = Profile()
        app_.show()

        sys.excepthook = except_hook
        sys.exit(app.exec())
