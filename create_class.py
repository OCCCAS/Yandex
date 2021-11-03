import datetime

from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QHeaderView

from py_ui.create_class import Ui_Form
from service import *


class CreateClassTab(QWidget, Ui_Form):
    def __init__(self):
        super(CreateClassTab, self).__init__()

        self.setupUi(self)
        self.fill_names_combobox()
        self.setup_table()

        self.btn_add.clicked.connect(self.add_children_to_class_table_and_refill_names_combobox)
        self.btn_create_class.clicked.connect(self.create_class)

    def setup_table(self):
        table_header = self.tbl_class.horizontalHeader()

        table_header.setSectionResizeMode(0, QHeaderView.Stretch)
        table_header.setSectionResizeMode(1, QHeaderView.Stretch)
        table_header.setSectionResizeMode(2, QHeaderView.ResizeToContents)

    def create_class(self):
        children_list = self.get_children_emails_list_from_table()
        res_code = create_class(children_list)

        if res_code and len(children_list) > 0:
            QMessageBox().information(self, 'Успешно!',
                                      f'Класс из {len(children_list)} учеников успешно создан!')

    def get_children_emails_list_from_table(self) -> List[str]:
        emails = []

        for row_ind in range(self.tbl_class.rowCount()):
            email = self.tbl_class.item(row_ind, 1).text()
            emails.append(email)

        return emails

    def add_children_to_class_table_and_refill_names_combobox(self):
        if self.is_children_selected():
            name = self.get_selected_children_name()
            *name, email = name.split(' ')

            name = ' '.join(name)
            # delete brackets (email) -> email
            email = email[1:-1]

            birthday_timestamp = get_user_data_by_column('birthday', email)
            birthday = datetime.datetime.fromtimestamp(birthday_timestamp).strftime('%d.%m.%Y')

            self.add_to_table(name, email, birthday)
            self.fill_names_combobox()

    def add_to_table(self, name, email, birthday):
        self.tbl_class.setRowCount(self.tbl_class.rowCount() + 1)

        for i, el in enumerate((name, email, birthday)):
            self.tbl_class.setItem(self.tbl_class.rowCount() - 1, i, QTableWidgetItem(str(el)))

    def is_children_selected(self) -> bool:
        default_cmb_value = get_static_interface_texts('default_names_combobox_values')

        if self.get_selected_children_name() == default_cmb_value:
            return False

        return True

    def get_selected_children_name(self) -> str:
        return self.cmb_name.currentText()

    def is_children_added_to_current_class(self, email: str) -> bool:
        """Is children added to current class"""
        email_column_index = 1
        for row_index in range(self.tbl_class.rowCount()):
            user_email_from_table = self.tbl_class.item(row_index, email_column_index).text() 
            
            if user_email_from_table == email:
                return True

        return False

    def add_default_name_to_names_combobox(self):
        default_cmb_value = get_static_interface_texts('default_names_combobox_values')
        self.cmb_name.addItem(default_cmb_value)

    def fill_names_combobox(self):
        children_list = get_children_list()

        self.cmb_name.clear()
        self.add_default_name_to_names_combobox()

        for children in children_list:
            # if children not in class
            first_name, last_name, email, class_ = *children[1:4], children[10]
            if not class_ and not self.is_children_added_to_current_class(email):
                text = f'{first_name} {last_name} ({email})'
                self.cmb_name.addItem(text)
