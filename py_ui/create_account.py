# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/create_account.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(489, 486)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 10, 421, 397))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.edit_name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edit_name.setObjectName("edit_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.edit_name)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.edit_surname = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edit_surname.setObjectName("edit_surname")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.edit_surname)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.edit_nick = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edit_nick.setObjectName("edit_nick")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.edit_nick)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.dtchoice_birthday = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.dtchoice_birthday.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dtchoice_birthday.setCalendarPopup(False)
        self.dtchoice_birthday.setCurrentSectionIndex(0)
        self.dtchoice_birthday.setTimeSpec(QtCore.Qt.LocalTime)
        self.dtchoice_birthday.setObjectName("dtchoice_birthday")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dtchoice_birthday)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.cmb_gender = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.cmb_gender.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.cmb_gender.setCurrentText("")
        self.cmb_gender.setObjectName("cmb_gender")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.cmb_gender)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.cmb_post = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.cmb_post.setObjectName("cmb_post")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.cmb_post)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.edit_password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edit_password.setObjectName("edit_password")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.edit_password)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.edit_password_again = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edit_password_again.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edit_password_again.setObjectName("edit_password_again")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.edit_password_again)
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.textBrowser.setObjectName("textBrowser")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.textBrowser)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(9, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        self.verticalLayout.addLayout(self.formLayout)
        self.btn_create_account = QtWidgets.QPushButton(Form)
        self.btn_create_account.setGeometry(QtCore.QRect(260, 450, 200, 25))
        self.btn_create_account.setObjectName("btn_create_account")
        self.lbl_error = QtWidgets.QLabel(Form)
        self.lbl_error.setGeometry(QtCore.QRect(40, 420, 421, 17))
        self.lbl_error.setStyleSheet("color: red;")
        self.lbl_error.setText("")
        self.lbl_error.setObjectName("lbl_error")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_9.setText(_translate("Form", "Регистрация"))
        self.label.setText(_translate("Form", "Имя:"))
        self.label_5.setText(_translate("Form", "Фамилия:"))
        self.label_4.setText(_translate("Form", "Псевдоним:"))
        self.label_6.setText(_translate("Form", "Дата рождения:"))
        self.label_7.setText(_translate("Form", "Пол:"))
        self.label_8.setText(_translate("Form", "Должность:"))
        self.label_3.setText(_translate("Form", "Пароль:"))
        self.label_2.setText(_translate("Form", "Пароль еще раз:"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Требования к паролю:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Длина пароля не менее 9 символов</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Буквы разного регистра</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Цифры в парлу</li></ul></body></html>"))
        self.btn_create_account.setText(_translate("Form", "Зарегестрироваться"))
