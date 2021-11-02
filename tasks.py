import datetime

from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QFileDialog, QMessageBox

from py_ui import profile_teacher
from service import *


class ManageTasksTab(QWidget, profile_teacher.Ui_Form):
    def __init__(self, parent=None):
        super(QWidget, self).__init__()

        self.setupUi(parent)

        self.__material_photo = None
        self.btn_add_material.clicked.connect(self.choice_photo)
        self.btn_send.clicked.connect(self.send_task)

    def get_title(self) -> str:
        return self.edit_title.text()

    def get_task_text(self) -> str:
        return self.edit_text.toPlainText()

    def get_task_date(self) -> int:
        date = self.dtchoice_date.date().toPyDate()
        datetime_ = datetime.datetime.combine(date, datetime.time())
        return int(datetime_.timestamp())

    def get_material_photo(self) -> str:
        return self.__material_photo if self.__material_photo else None

    def choice_photo(self) -> None:
        file_name = QFileDialog.getOpenFileName(self, 'Выбрать фотографию', '',
                                                'Картинка (*.jpg, *.png);;Все файлы (*)')[0]

        self.__material_photo = file_name

    def send_task(self) -> None:
        title = self.get_title()
        text = self.get_task_text()
        date = self.get_task_date()
        photo = self.get_material_photo()

        created = create_task(title, text, date, photo)

        if created:
            if QMessageBox.information(self, 'Успешно!', 'Задача успешно отправлена'):
                self.clear_all_fields()

    def clear_all_fields(self):
        self.edit_title.clear()
        self.edit_text.clear()
        self.__material_photo = None
        self.btn_add_material.setText('Загрузить пример, материал')


class TasksTab(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.setupUi(parent)
        self.fill_table()

    def fill_table(self):
        tasks = self.get_tasks()

        self.tbl_tasks.setRowCount(0)
        for i, row in enumerate(tasks):
            self.tbl_tasks.setRowCount(self.tbl_tasks.rowCount() + 1)
            for j, el in enumerate(row):
                self.tbl_tasks.setItem(i, j, QTableWidgetItem(str(el)))

    @staticmethod
    def get_tasks() -> List[List]:
        tasks = [list(task) for task in get_tasks()]

        for i, task in enumerate(tasks):
            for j, elem in enumerate(task):
                # If elem column index is date columns index in table, format datetime timestamp
                elem = datetime.datetime.fromtimestamp(elem).strftime('%d.%m.%Y') if j == 3 else elem
                elem = '' if elem is None else elem

                tasks[i][j] = elem

            # in database: (0) id, (1) title, (2) text, (3) date, (4) photo
            # in our table: (0) date, (1) title, (2) text, (3) photo
            tasks[i] = [task[3], *task[1:3], task[4]]

        return tasks
