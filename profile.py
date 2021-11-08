from add_to_portfolio import AddToPortfolio
from edit_profile import EditProfile
from edit_portfolio import EditPortfolio
from create_and_login_account import CreateAccountApp
from py_ui.profile import Ui_Form

from qportfoliofeed import *

from service import *

from PyQt5.Qt import QImage
from PyQt5.QtWidgets import QMessageBox
from PIL.ImageQt import ImageQt


class ProfileTab(QWidget, Ui_Form):
    def __init__(self):
        super(ProfileTab, self).__init__()

        self.setupUi(self)
        self.fill_profile()
        self.fill_portfolio()

        self.btn_add_img_to_portfolio.clicked.connect(self.add_to_portfolio)
        self.btn_edit_profile.clicked.connect(self.edit_profile)
        self.btn_delete_profile.clicked.connect(self.delete_profile)
        self.btn_exit.clicked.connect(self.exit_from_profile)
        self.btn_edit_portfolio.clicked.connect(self.edit_portfolio)

    def edit_portfolio(self):
        edit_portfolio_dialog = EditPortfolio()
        edit_portfolio_dialog.exec_()
        self.fill_portfolio()

    def close_main_window_and_start_login(self):
        # ProfileTab (self) > QStackWidget (self.parent()) > QTabWidget (self.parent().parent()) > QMainWindow (self.parent().parent().parent())
        main_window = self.parent().parent().parent()
        create_account_app = CreateAccountApp()
        main_window.close()
        create_account_app.exec_()

    def exit_from_profile(self):
        """Exit from current profile"""
        ans = QMessageBox.question(self, 'Уверены?', 'Вы точно хотите выйти из своего профиля?')
        if ans == QMessageBox.Yes:
            exit_from_local()
            self.close_main_window_and_start_login()

    def delete_profile(self) -> None:
        """Delete profile"""
        delete = QMessageBox.question(self, 'Удалить?', 'Вы точно хотите удалить свой аккаунт?')
        if delete == QMessageBox.Yes:
            delete_profile()
            exit_from_local()
            self.close_main_window_and_start_login()

    def edit_profile(self) -> None:
        """Open edit profile dialog and repaint profile info"""
        edit_profile_app = EditProfile()
        opened = edit_profile_app.exec_()

        if not opened:
            self.fill_profile()

    def add_to_portfolio(self) -> None:
        """Open add to portfolio dialog and repaint portfolio feed"""
        add_to_portfolio_app = AddToPortfolio()
        opened = add_to_portfolio_app.exec_()

        if not opened:
            self.fill_portfolio()
            self.fill_profile()

    def fill_portfolio(self):
        """Fill portfolio feed"""
        if self.feed_portfolio.widget().layout():
            self.feed_portfolio.clear_and_emit()

        user_portfolio_data = get_user_portfolio()

        for portfolio_data in user_portfolio_data:
            title, place, date, photo_path = portfolio_data[1:]
            self.feed_portfolio.add_item(
                PortfolioFeedItem(
                    PortfolioItem(title, photo_path, date, place)
                )
            )

        self.feed_portfolio.create_()

    @staticmethod
    def get_profile_info() -> dict:
        """Get name and age in dict format"""
        user_email = get_local_user_email()

        name, surname, birthday_timestamp = get_user_data_by_columns(
            ['name', 'surname', 'birthday'],
            user_email
        )
        birthday_datetime = datetime.datetime.fromtimestamp(birthday_timestamp)
        # Now datetime minus birthday datetime, then get days and divide it to days count in year
        days_in_year = 365
        age = (datetime.datetime.now() - birthday_datetime).days // days_in_year

        return {'name': f'{name} {surname}', 'age': age}

    def set_profile_photo(self) -> None:
        """Set profile avatar photo"""
        image = Image.open(get_user_avatar_photo())
        image = image.resize((self.lbl_profile_image.maximumWidth(), self.lbl_profile_image.maximumHeight()))
        image = rounded_image(image)
        image.convert('RGBA')
        pixmap = QPixmap().fromImage(QImage(ImageQt(image)))
        self.lbl_profile_image.setPixmap(pixmap)

    def fill_profile(self) -> None:
        """Fill all profile info (photo, name, age and etc.)"""
        profile_info = self.get_profile_info()
        self.lbl_name.setText(profile_info.get('name'))
        self.lbl_name.adjustSize()

        self.lbl_age.setText('Возраст: ' + str(profile_info.get('age')))
        self.lbl_age.adjustSize()
        self.set_profile_photo()
