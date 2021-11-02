# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/create_class.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(561, 495)
        Dialog.setStyleSheet("background-color: white")
        self.tbl_class = QtWidgets.QTableWidget(Dialog)
        self.tbl_class.setGeometry(QtCore.QRect(10, 60, 541, 251))
        self.tbl_class.setObjectName("tbl_class")
        self.tbl_class.setColumnCount(3)
        self.tbl_class.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_class.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_class.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_class.setHorizontalHeaderItem(2, item)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 541, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #333c56;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 320, 541, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #333c56;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 370, 541, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cmb_name = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.cmb_name.setStyleSheet("background-color: #ffffff;\n"
"border-radius: 5px;\n"
"color: black;\n"
"padding: 10px;\n"
"border: 2px solid #eeeeee;\n"
"\n"
"")
        self.cmb_name.setObjectName("cmb_name")
        self.cmb_name.addItem("")
        self.horizontalLayout.addWidget(self.cmb_name)
        self.btn_add = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_add.setFont(font)
        self.btn_add.setStyleSheet("background-color: #eeeeee;\n"
"border-radius: 5px;\n"
"color: black;\n"
"padding: 10px;\n"
"border: 2px solid #eeeeee;\n"
"")
        self.btn_add.setObjectName("btn_add")
        self.horizontalLayout.addWidget(self.btn_add)
        self.btn_create_class = QtWidgets.QPushButton(Dialog)
        self.btn_create_class.setGeometry(QtCore.QRect(284, 445, 266, 37))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_create_class.setFont(font)
        self.btn_create_class.setStyleSheet("padding: 10px;\n"
"background-color: #4654f9;\n"
"border-width: 2px;\n"
"border-radius: 5px;\n"
"color: white;\n"
"")
        self.btn_create_class.setObjectName("btn_create_class")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.tbl_class.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Имя"))
        item = self.tbl_class.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Почта"))
        item = self.tbl_class.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "День рождения"))
        self.label.setText(_translate("Dialog", "Ваш класс:"))
        self.label_2.setText(_translate("Dialog", "Добавить ребенка:"))
        self.cmb_name.setItemText(0, _translate("Dialog", "<Имя>"))
        self.btn_add.setText(_translate("Dialog", "Добавить"))
        self.btn_create_class.setText(_translate("Dialog", "Создать класс"))
