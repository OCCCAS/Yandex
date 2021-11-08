import sys
import datetime

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from py_ui.edit_portfolio import Ui_Dialog

from service import *
from config import *


class EditPortfolio(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fill_portfolio_list()
        self.btn_delete.clicked.connect(self.delete_portfolio_item)
    
    def delete_portfolio_item(self):
        ans = QMessageBox.question(self, 'Уверены?', 'Вы точно хотите удалить это и из своего портфолио?')
        if ans == QMessageBox.Yes:
            selected_row = self.list_portfolio.currentRow()
            selected_row_text = self.list_portfolio.item(selected_row).text()
            selected_row_data = selected_row_text.split('; ')
            data = {
                'competitions_name': selected_row_data[0],
                'place': selected_row_data[1],
                'datetime': int(datetime.datetime.strptime(selected_row_data[2], '%d.%m.%Y').timestamp())
            }
            delete_portfolio_item(data)
            QMessageBox.information(self, 'Успешно!', 'Это удалено с вашего портфолио')
            self.remove_from_list(selected_row)

    def remove_from_list(self, row_index):
        self.list_portfolio.takeItem(row_index)

    def fill_portfolio_list(self):
        user_portfolio = get_user_portfolio()
        for portfolio_item in user_portfolio:
            competitions_name = portfolio_item[1]
            place = portfolio_item[2]
            datetime_ = datetime.datetime.fromtimestamp(portfolio_item[3]).strftime('%d.%m.%Y')
            self.list_portfolio.addItem(f'{competitions_name}; {place}; {datetime_}')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app_ = EditPortfolio()
    app_.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
