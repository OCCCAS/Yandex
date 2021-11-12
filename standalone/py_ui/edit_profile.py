# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/edit_profile.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(405, 286)
        Dialog.setStyleSheet("background-color: white;")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.edit_name = QtWidgets.QLineEdit(Dialog)
        self.edit_name.setStyleSheet("background-color: #ffffff;\n"
"border-radius: 5px;\n"
"color: black;\n"
"padding: 10px;\n"
"border: 2px solid #eeeeee;\n"
"\n"
"")
        self.edit_name.setObjectName("edit_name")
        self.horizontalLayout.addWidget(self.edit_name)
        self.edit_surname = QtWidgets.QLineEdit(Dialog)
        self.edit_surname.setStyleSheet("background-color: #ffffff;\n"
"border-radius: 5px;\n"
"color: black;\n"
"padding: 10px;\n"
"border: 2px solid #eeeeee;\n"
"\n"
"")
        self.edit_surname.setObjectName("edit_surname")
        self.horizontalLayout.addWidget(self.edit_surname)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.cmb_gender = QtWidgets.QComboBox(Dialog)
        self.cmb_gender.setStyleSheet("background-color: #ffffff;\n"
"border-radius: 5px;\n"
"color: black;\n"
"padding: 10px;\n"
"border: 2px solid #eeeeee;\n"
"\n"
"")
        self.cmb_gender.setObjectName("cmb_gender")
        self.cmb_gender.addItem("")
        self.cmb_gender.addItem("")
        self.verticalLayout.addWidget(self.cmb_gender)
        self.dtchoice_birthday = QtWidgets.QDateEdit(Dialog)
        self.dtchoice_birthday.setStyleSheet("background-color: #ffffff;\n"
"border-radius: 5px;\n"
"color: black;\n"
"padding: 10px;\n"
"border: 2px solid #eeeeee;\n"
"\n"
"")
        self.dtchoice_birthday.setObjectName("dtchoice_birthday")
        self.verticalLayout.addWidget(self.dtchoice_birthday)
        self.btn_add_photo = QtWidgets.QPushButton(Dialog)
        self.btn_add_photo.setStyleSheet("background-color: #eeeeee;\n"
"border-radius: 5px;\n"
"color: black;\n"
"padding: 10px;\n"
"border: 2px solid #eeeeee;\n"
"")
        self.btn_add_photo.setObjectName("btn_add_photo")
        self.verticalLayout.addWidget(self.btn_add_photo)
        self.btn_save_edits = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_save_edits.setFont(font)
        self.btn_save_edits.setStyleSheet("padding: 10px;\n"
"background-color: #4654f9;\n"
"border-width: 2px;\n"
"border-radius: 5px;\n"
"color: white;\n"
"")
        self.btn_save_edits.setObjectName("btn_save_edits")
        self.verticalLayout.addWidget(self.btn_save_edits)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.edit_name.setPlaceholderText(_translate("Dialog", "Имя"))
        self.edit_surname.setPlaceholderText(_translate("Dialog", "Фамилия"))
        self.cmb_gender.setItemText(0, _translate("Dialog", "Мальчик"))
        self.cmb_gender.setItemText(1, _translate("Dialog", "Девочка"))
        self.btn_add_photo.setText(_translate("Dialog", "Добавить фотографию"))
        self.btn_save_edits.setText(_translate("Dialog", "Сохранить изменения"))