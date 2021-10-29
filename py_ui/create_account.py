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
        Form.resize(887, 599)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        Form.setFont(font)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color: white;")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(520, 120, 341, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.edit_name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edit_name.setStyleSheet("background-color: #ffffff;\n"
"border-radius: 5px;\n"
"color: black;\n"
"padding: 10px;\n"
"border: 2px solid #eeeeee;\n"
"\n"
"")
        self.edit_name.setObjectName("edit_name")
        self.horizontalLayout.addWidget(self.edit_name)
        self.edit_surname = QtWidgets.QLineEdit(self.verticalLayoutWidget)
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
        self.edit_email = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edit_email.setStyleSheet("background-color: #ffffff;\n"
"border-radius: 5px;\n"
"color: black;\n"
"padding: 10px;\n"
"border: 2px solid #eeeeee;\n"
"\n"
"")
        self.edit_email.setObjectName("edit_email")
        self.verticalLayout.addWidget(self.edit_email)
        self.cmb_gender = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.cmb_gender.setStyleSheet("background-color: #ffffff;\n"
"border-radius: 5px;\n"
"color: black;\n"
"padding: 10px;\n"
"border: 2px solid #eeeeee;\n"
"\n"
"")
        self.cmb_gender.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.cmb_gender.setEditable(False)
        self.cmb_gender.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.cmb_gender.setIconSize(QtCore.QSize(16, 16))
        self.cmb_gender.setDuplicatesEnabled(False)
        self.cmb_gender.setFrame(True)
        self.cmb_gender.setObjectName("cmb_gender")
        self.cmb_gender.addItem("")
        self.cmb_gender.addItem("")
        self.verticalLayout.addWidget(self.cmb_gender)
        self.dtchoice_birthday = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setKerning(False)
        self.dtchoice_birthday.setFont(font)
        self.dtchoice_birthday.setStyleSheet("background-color: #ffffff;\n"
"border-radius: 5px;\n"
"color: black;\n"
"padding: 10px;\n"
"border: 2px solid #eeeeee;\n"
"\n"
"")
        self.dtchoice_birthday.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.dtchoice_birthday.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dtchoice_birthday.setCalendarPopup(False)
        self.dtchoice_birthday.setCurrentSectionIndex(0)
        self.dtchoice_birthday.setTimeSpec(QtCore.Qt.LocalTime)
        self.dtchoice_birthday.setObjectName("dtchoice_birthday")
        self.verticalLayout.addWidget(self.dtchoice_birthday)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.edit_password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edit_password.setStyleSheet("background-color: #ffffff;\n"
"border-radius: 5px;\n"
"color: black;\n"
"padding: 10px;\n"
"border: 2px solid #eeeeee;\n"
"\n"
"")
        self.edit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edit_password.setObjectName("edit_password")
        self.horizontalLayout_2.addWidget(self.edit_password)
        self.edit_password_again = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edit_password_again.setStyleSheet("background-color: #ffffff;\n"
"border-radius: 5px;\n"
"color: black;\n"
"padding: 10px;\n"
"border: 2px solid #eeeeee;\n"
"\n"
"")
        self.edit_password_again.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edit_password_again.setObjectName("edit_password_again")
        self.horizontalLayout_2.addWidget(self.edit_password_again)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.btn_add_photo = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_add_photo.setStyleSheet("background-color: #eeeeee;\n"
"border-radius: 5px;\n"
"color: black;\n"
"padding: 10px;\n"
"border: 2px solid #eeeeee;\n"
"")
        self.btn_add_photo.setObjectName("btn_add_photo")
        self.verticalLayout.addWidget(self.btn_add_photo)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 150, 450, 330))
        self.label.setMaximumSize(QtCore.QSize(450, 700))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ui/../images/reg-img.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(550, 20, 256, 46))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #333c56;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(550, 80, 155, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #babac1;")
        self.label_3.setObjectName("label_3")
        self.lbl_login = QClickableLabel(Form)
        self.lbl_login.setGeometry(QtCore.QRect(750, 80, 52, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_login.setFont(font)
        self.lbl_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lbl_login.setStyleSheet("color: #4654f9;")
        self.lbl_login.setObjectName("lbl_login")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 30, 175, 46))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #333c56;")
        self.label_4.setObjectName("label_4")
        self.lbl_error = QtWidgets.QLabel(Form)
        self.lbl_error.setGeometry(QtCore.QRect(520, 450, 339, 31))
        self.lbl_error.setStyleSheet("color: red;")
        self.lbl_error.setText("")
        self.lbl_error.setObjectName("lbl_error")
        self.btn_create_account = QtWidgets.QPushButton(Form)
        self.btn_create_account.setGeometry(QtCore.QRect(520, 510, 339, 37))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_create_account.setFont(font)
        self.btn_create_account.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_create_account.setStyleSheet("padding: 10px;\n"
"background-color: #4654f9;\n"
"border-width: 2px;\n"
"border-radius: 5px;\n"
"color: white;\n"
"")
        self.btn_create_account.setObjectName("btn_create_account")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.edit_name.setPlaceholderText(_translate("Form", "Имя"))
        self.edit_surname.setPlaceholderText(_translate("Form", "Фамилия"))
        self.edit_email.setPlaceholderText(_translate("Form", "Почта"))
        self.cmb_gender.setItemText(0, _translate("Form", "Мальчик"))
        self.cmb_gender.setItemText(1, _translate("Form", "Девочка"))
        self.dtchoice_birthday.setDisplayFormat(_translate("Form", "dd.MM.yyyy"))
        self.edit_password.setPlaceholderText(_translate("Form", "Пароль"))
        self.edit_password_again.setPlaceholderText(_translate("Form", "Пароль еще раз"))
        self.btn_add_photo.setText(_translate("Form", "Добавить фотографию"))
        self.label_2.setText(_translate("Form", "Регистриция"))
        self.label_3.setText(_translate("Form", "Уже есть аккаунт?"))
        self.lbl_login.setText(_translate("Form", "Войти"))
        self.label_4.setText(_translate("Form", "PortSave"))
        self.btn_create_account.setText(_translate("Form", "Зарегестрироваться"))
from qclickablelabel import QClickableLabel
