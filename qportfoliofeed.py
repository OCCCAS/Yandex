import datetime

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextBrowser, QLabel, QScrollArea


class PortfolioItem:
    def __init__(self, title: str, photo_path: str, date_timestamp: int, place: str):
        self._title = title
        self._photo_path = photo_path
        self._datetime: datetime.datetime = datetime.datetime.fromtimestamp(date_timestamp)
        self._place = place

    def get_formatted_as_html_data(self) -> dict:
        """This function return data, but data items return as html for example: <h3 align=center>{title}</h3>'"""
        return {
            'title': f'<h2 align=center>{self._title}</h2>',
            'photo_path': self._photo_path,
            'date': f'<h4>{self._datetime.strftime("%d.%m.%Y")}</h4>',
            'place': f'<h3>{self._place}</h3>'
        }


class PortfolioFeedItem(QWidget):
    def __init__(self, portfolio_item: PortfolioItem):
        super().__init__()
        self.portfolio_item: PortfolioItem = portfolio_item
        self.__init()

    def __init(self):
        self.setLayout(QVBoxLayout(self))
        data_widgets = self.__get_data_as_widgets()
        self.layout().addWidget(data_widgets.get('title'))
        self.layout().addSpacing(5)
        self.layout().addWidget(data_widgets.get('photo'))
        self.layout().addSpacing(5)
        self.layout().addWidget(data_widgets.get('description'))

    def __get_data_as_widgets(self) -> dict:
        data = self.portfolio_item.get_formatted_as_html_data()

        _title = QTextBrowser()
        _title.setText(data.get('title'))
        _title.setStyleSheet('background-color: rgba(0, 0, 0, 0);')

        _photo = QLabel()
        _photo.setAlignment(Qt.AlignCenter)
        _photo.setPixmap(QPixmap(data.get('photo_path')).scaledToWidth(self.width() // 2))

        _description = QTextBrowser()
        _description.setText(f"{data.get('place')}{data.get('date')}")
        _description.setStyleSheet('background-color: rgba(0, 0, 0, 0);')

        return {
            'title': _title,
            'photo': _photo,
            'description': _description
        }


class QPortfolioFeed(QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.emit()

    def emit(self):
        self.feed_widget_layout = QVBoxLayout()

    def add_item(self, item: PortfolioFeedItem) -> None:
        self.feed_widget_layout.addWidget(item)
        self.feed_widget_layout.addSpacing(20)

    def create(self):
        self.feed_widget = QWidget()
        self.feed_widget.setLayout(self.feed_widget_layout)
        self.setWidget(self.feed_widget)

    def clear_and_emit(self) -> None:
        self.feed_widget.setParent(None)
        self.emit()
