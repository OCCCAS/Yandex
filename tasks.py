import datetime
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QFileDialog, QMessageBox

from service import *


class ManageTasks(QWidget):
    def __init__(self):
        super().__init__()
        self.__material_photo = None

        self.setupUi(self)

        self.btn_add_material.clicked.connect(self.__choice_photo)
        self.btn_send.clicked.connect(self.__send_task)

    def __get_title(self) -> str:
        return self.edit_title.text()

    def __get_task_text(self) -> str:
        return self.edit_text.toPlainText()

    def __get_task_date(self) -> int:
        date = self.dtchoice_date.date().toPyDate()
        datetime_ = datetime.datetime.combine(date, datetime.time())
        return int(datetime_.timestamp())

    def __get_material_photo(self) -> str:
        return self.__material_photo if self.__material_photo else None

    def __choice_photo(self) -> None:
        file_name = QFileDialog.getOpenFileName(self, 'Выбрать фотографию', '',
                                                'Картинка (*.jpg, *.png);;Все файлы (*)')[0]

        self.__material_photo = file_name

    def __send_task(self) -> None:
        title = self.__get_title()
        text = self.__get_task_text()
        date = self.__get_task_date()
        photo = self.__get_material_photo()

        created = create_task(title, text, date, photo)

        if created:
            if QMessageBox.information(self, 'Успешно!', 'Задача успешно отправлена'):
                self.close()


class Tasks(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.__fill_table()

    def __fill_table(self):
        tasks = self.__get_tasks()

        self.tbl_tasks.setRowCount(0)
        for i, row in enumerate(tasks):
            self.tbl_tasks.setRowCount(self.tbl_tasks.rowCount() + 1)
            for j, el in enumerate(row):
                self.tbl_tasks.setItem(i, j, QTableWidgetItem(str(el)))

    @staticmethod
    def __get_tasks() -> List[List]:
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


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    post = 2
    if post == 1:
        from py_ui.manage_tasks import Ui_Form

        App = ManageTasks
    elif post == 2:
        from py_ui.tasks import Ui_Form

        App = Tasks

    App.__bases__ = App.__bases__ + (Ui_Form,)

    app_ = App()
    app_.show()

    sys.excepthook = except_hook
    sys.exit(app.exec())
