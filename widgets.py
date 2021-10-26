from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel


class ClickableLabel(QLabel):
    clicked = QtCore.pyqtSignal()
 
    def mousePressEvent(self, QMouseEvent):
        self.clicked.emit()
        QLabel.mousePressEvent(self, QMouseEvent)

