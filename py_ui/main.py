# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(940, 646)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tbl_scedule_left = QtWidgets.QTableWidget(self.centralwidget)
        self.tbl_scedule_left.setGeometry(QtCore.QRect(10, 10, 300, 500))
        self.tbl_scedule_left.setObjectName("tbl_scedule_left")
        self.tbl_scedule_left.setColumnCount(0)
        self.tbl_scedule_left.setRowCount(0)
        self.tbl_scedule_right = QtWidgets.QTableWidget(self.centralwidget)
        self.tbl_scedule_right.setGeometry(QtCore.QRect(310, 10, 300, 500))
        self.tbl_scedule_right.setObjectName("tbl_scedule_right")
        self.tbl_scedule_right.setColumnCount(0)
        self.tbl_scedule_right.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 940, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
