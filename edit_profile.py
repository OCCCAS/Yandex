import sys
import datetime

from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
from py_ui.edit_profile import Ui_Dialog

from service import *
from config import *


class EditProfile(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.profile_photo = None

        self.setupUi(self)
        self.fill_all_fields()

        self.btn_add_photo.clicked.connect(self.choose_photo)
        self.btn_save_edits.clicked.connect(self.edit_profile)

    def fill_all_fields(self):
        user_data = get_full_user_data()
        name = user_data[1]
        surname = user_data[2]
        birthday = datetime.datetime.fromtimestamp(user_data[4])
        cmb_gender_all_items = [self.cmb_gender.itemText(i) for i in range(self.cmb_gender.count())]
        gender = [item for item in cmb_gender_all_items if item.startswith(user_data[5])][0]
        gender_index = self.cmb_gender.findText(gender)

        self.edit_name.setText(str(name))
        self.edit_surname.setText(str(surname))
        self.cmb_gender.setCurrentIndex(gender_index)
        self.dtchoice_birthday.setDate(birthday.date())

    def get_birthday_timestamp(self):
        date = self.dtchoice_birthday.date().toPyDate()
        datetime_ = datetime.datetime.combine(date, datetime.time(0, 0, 0))
        return int(datetime_.timestamp())

    def get_fields_data(self):
        data = {
            'name': self.edit_name.text(),
            'surname': self.edit_surname.text(),
            'gender': self.cmb_gender.currentText()[0],
            'birthday': self.get_birthday_timestamp(),
            'photo': self.profile_photo if self.profile_photo else None
        }

        return data

    def edit_profile(self):
        data = self.get_fields_data()
        edit_profile(*list(data.values()))
        self.close()

    def choose_photo(self):
        file_name = QFileDialog.getOpenFileName(self, 'Выбрать фотографию', '',
                                                'Картинка jpg (*.jpg);;Картинка png (*.png);;Все файлы (*)')[0]

        self.profile_photo = file_name


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app_ = EditProfile()
    app_.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
