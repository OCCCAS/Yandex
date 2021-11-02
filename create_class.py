import datetime

from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox

from py_ui import profile_teacher
from service import *


class CreateClassTab(QWidget, profile_teacher.Ui_Form):
    def __init__(self, parent=None):
        super(QWidget, self).__init__()
        self.setupUi(parent)

        self.fill_name_combobox()

        self.btn_add.clicked.connect(self.add_children_to_class_table)
        self.btn_create_class.clicked.connect(self.create_class)

    def create_class(self):
        children_list = self.get_children_emails_list()
        res_code = create_class(children_list)

        if res_code and len(children_list) > 0:
            QMessageBox().information(self, 'Успешно!',
                                      f'Класс из {len(children_list)} учеников успешно создан!')

    def get_children_emails_list(self) -> List[str]:
        emails = []

        for row_ind in range(self.tbl_class.rowCount()):
            email = self.tbl_class.item(row_ind, 1).text()
            emails.append(email)

        return emails

    def add_children_to_class_table(self):
        if self.is_children_selected():
            name = self.get_selected_children_name()
            *_, email = name.split(' ')
            # "(email)"[1:-1] = "email"
            email = email[1:-1]

            birthday_timestamp = get_user_data_by_column('birthday', email)
            birthday = datetime.datetime.fromtimestamp(birthday_timestamp).strftime('%d.%m.%Y')

            self.add_to_table(name, email, birthday)

    def add_to_table(self, name, email, birthday):
        self.tbl_class.setRowCount(self.tbl_class.rowCount() + 1)

        for i, el in enumerate((name, email, birthday)):
            self.tbl_class.setItem(self.tbl_class.rowCount() - 1, i, QTableWidgetItem(str(el)))

    def is_children_selected(self) -> bool:
        default_cmb_value = '<Имя>'

        if self.get_selected_children_name() == default_cmb_value:
            return False

        return True

    def get_selected_children_name(self) -> str:
        return self.cmb_name.currentText()

    def fill_name_combobox(self):
        children_list = get_children_list()

        for children in children_list:
            class_ = children[10]
            if not class_:
                first_name, last_name, email = children[1:4]
                text = f'{first_name} {last_name} ({email})'
                self.cmb_name.addItem(text)
