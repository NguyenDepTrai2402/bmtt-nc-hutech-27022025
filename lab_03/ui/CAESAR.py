# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/CAESAR.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "../platforms"
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 30, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 120, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 260, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 320, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.txt_plaintext = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_plaintext.setGeometry(QtCore.QRect(250, 120, 501, 71))
        self.txt_plaintext.setObjectName("txt_plaintext")
        self.txt_key = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_key.setGeometry(QtCore.QRect(250, 270, 501, 31))
        self.txt_key.setObjectName("txt_key")
        self.txt_ciphertext = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_ciphertext.setGeometry(QtCore.QRect(250, 330, 501, 71))
        self.txt_ciphertext.setObjectName("txt_ciphertext")
        self.btn_encrypt = QtWidgets.QToolButton(self.centralwidget)
        self.btn_encrypt.setGeometry(QtCore.QRect(260, 480, 101, 31))
        self.btn_encrypt.setObjectName("btn_encrypt")
        self.btn_decrypt = QtWidgets.QToolButton(self.centralwidget)
        self.btn_decrypt.setGeometry(QtCore.QRect(580, 480, 101, 31))
        self.btn_decrypt.setObjectName("btn_decrypt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "CAESAR CIPHER"))
        self.label_2.setText(_translate("MainWindow", "Plain Text:"))
        self.label_3.setText(_translate("MainWindow", "Key:"))
        self.label_4.setText(_translate("MainWindow", "CipherText:"))
        self.btn_encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.btn_decrypt.setText(_translate("MainWindow", "Decrypt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
