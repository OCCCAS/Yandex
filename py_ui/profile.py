# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/profile.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(506, 779)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 481, 131))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tb_profile_info = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.tb_profile_info.setObjectName("tb_profile_info")
        self.horizontalLayout.addWidget(self.tb_profile_info)
        self.btn_add_img_to_portfolio = QtWidgets.QPushButton(Form)
        self.btn_add_img_to_portfolio.setGeometry(QtCore.QRect(10, 150, 212, 25))
        self.btn_add_img_to_portfolio.setObjectName("btn_add_img_to_portfolio")
        self.feed_portfolio = QtWidgets.QScrollArea(Form)
        self.feed_portfolio.setGeometry(QtCore.QRect(10, 190, 481, 571))
        self.feed_portfolio.setWidgetResizable(True)
        self.feed_portfolio.setObjectName("feed_portfolio")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 479, 569))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.feed_portfolio.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_add_img_to_portfolio.setText(_translate("Form", "Добавить фото в портфолио"))