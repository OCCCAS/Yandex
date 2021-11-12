# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/create_class.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(581, 590)
        Form.setStyleSheet("background-color: white;")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #333c56;")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tbl_class = QtWidgets.QTableWidget(Form)
        self.tbl_class.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tbl_class.setObjectName("tbl_class")
        self.tbl_class.setColumnCount(3)
        self.tbl_class.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_class.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_class.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_class.setHorizontalHeaderItem(2, item)
        self.tbl_class.horizontalHeader().setCascadingSectionResizes(False)
        self.verticalLayout.addWidget(self.tbl_class)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #333c56;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cmb_name = QtWidgets.QComboBox(Form)
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
        self.btn_add_people = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btn_add_people.setFont(font)
        self.btn_add_people.setStyleSheet("background-color: #eeeeee;\n"
"border-radius: 5px;\n"
"color: black;\n"
"padding: 10px;\n"
"border: 2px solid #eeeeee;\n"
"")
        self.btn_add_people.setObjectName("btn_add_people")
        self.horizontalLayout.addWidget(self.btn_add_people)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.btn_create_class = QtWidgets.QPushButton(Form)
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
        self.verticalLayout_2.addWidget(self.btn_create_class)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Ваш класс:"))
        item = self.tbl_class.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Имя"))
        item = self.tbl_class.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Почта"))
        item = self.tbl_class.horizontalHeaderItem(2)
        item.setText(_translate("Form", "День рождения"))
        self.label_2.setText(_translate("Form", "Добавить ребенка:"))
        self.cmb_name.setItemText(0, _translate("Form", "<Имя>"))
        self.btn_add_people.setText(_translate("Form", "Добавить ученика"))
        self.btn_create_class.setText(_translate("Form", "Создать класс"))