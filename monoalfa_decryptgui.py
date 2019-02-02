# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monoalfa_decrypt1.0.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BrownFox(object):
    def setupUi(self, BrownFox):
        BrownFox.setObjectName("BrownFox")
        BrownFox.resize(761, 545)
        BrownFox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/brown-fox.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BrownFox.setWindowIcon(icon)
        BrownFox.setStyleSheet("background-image: url(:/images/brown-fox.png);")
        self.centralwidget = QtWidgets.QWidget(BrownFox)
        self.centralwidget.setObjectName("centralwidget")
        self.freq_Text_Box = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.freq_Text_Box.setGeometry(QtCore.QRect(240, 430, 256, 41))
        self.freq_Text_Box.setStyleSheet("background-color: rgba(59, 46, 34, 174);\n"
"color: rgb(255, 255, 255);")
        self.freq_Text_Box.setObjectName("freq_Text_Box")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 410, 101, 17))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 120, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 0, 67, 17))
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(240, 320, 254, 27))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Clear_Button = QtWidgets.QPushButton(self.layoutWidget)
        self.Clear_Button.setStyleSheet("\n"
"alternate-background-color: rgb(0, 0, 0);")
        self.Clear_Button.setObjectName("Clear_Button")
        self.horizontalLayout.addWidget(self.Clear_Button)
        self.Restart_Button = QtWidgets.QPushButton(self.layoutWidget)
        self.Restart_Button.setStyleSheet("alternate-background-color: rgb(0, 0, 0);")
        self.Restart_Button.setObjectName("Restart_Button")
        self.horizontalLayout.addWidget(self.Restart_Button)
        self.Decrypt_Button = QtWidgets.QPushButton(self.layoutWidget)
        self.Decrypt_Button.setStyleSheet("alternate-background-color: rgb(0, 0, 0);")
        self.Decrypt_Button.setObjectName("Decrypt_Button")
        self.horizontalLayout.addWidget(self.Decrypt_Button)
        self.Output_Text_Box = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Output_Text_Box.setGeometry(QtCore.QRect(30, 150, 699, 82))
        self.Output_Text_Box.setStyleSheet("background-color: rgba(59, 46, 34, 174);\n"
"color: rgb(255, 255, 255);")
        self.Output_Text_Box.setPlainText("")
        self.Output_Text_Box.setObjectName("Output_Text_Box")
        self.Input_Text_Box = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Input_Text_Box.setGeometry(QtCore.QRect(30, 30, 699, 81))
        self.Input_Text_Box.setStyleSheet("background-color: rgba(59, 46, 34, 174);\n"
"color: rgb(255, 255, 255);")
        self.Input_Text_Box.setObjectName("Input_Text_Box")
        BrownFox.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BrownFox)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 761, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        BrownFox.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BrownFox)
        self.statusbar.setObjectName("statusbar")
        BrownFox.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(BrownFox)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(BrownFox)
        QtCore.QMetaObject.connectSlotsByName(BrownFox)

    def retranslateUi(self, BrownFox):
        _translate = QtCore.QCoreApplication.translate
        BrownFox.setWindowTitle(_translate("BrownFox", "MainWindow"))
        self.freq_Text_Box.setPlainText(_translate("BrownFox", "etaoinsrhdlucmfywgpbvkxqjz"))
        self.label.setText(_translate("BrownFox", "Word Freqency"))
        self.label_2.setText(_translate("BrownFox", "Output"))
        self.label_3.setText(_translate("BrownFox", "Input"))
        self.Clear_Button.setText(_translate("BrownFox", "Clear"))
        self.Restart_Button.setText(_translate("BrownFox", "Restart"))
        self.Decrypt_Button.setText(_translate("BrownFox", "decrypt"))
        self.menuFile.setTitle(_translate("BrownFox", "File"))
        self.actionQuit.setText(_translate("BrownFox", "Quit"))
        self.actionQuit.setShortcut(_translate("BrownFox", "Ctrl+Q"))

import resources_rc
