#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# NyvoAI main module.
BY: NyvoStudio, KhodeNima ( Nima Bavar )
---
# This project and all of its components are licensed under the AGPL-3.0 ( GNU Affero Public License v3.0 ) license agreements.
"""


try:
    from PyQt5.QtWidgets import QDialog, QApplication
    from PyQt5 import QtCore, QtGui, QtWidgets
    import requests
    import sys
    
except ImportError:
    from os import system as cmd_input
    import importlib
    import time
    import sys
    
    cmd_input("cls")
    
    required_modules = ["requests", "PyQt5"]
    installed_modules = sys.modules.keys()
    
    for module in installed_modules:
        need_to_install = [module for module in required_modules if not module in installed_modules]
    
        
    for module in need_to_install:
        print("\33[31m Installing modules... \33[0m")
        
        cmd_input(f"pip install {module}")
        importlib.import_module(module)
        cmd_input("cls")
        
        
    time.sleep(10)
        
    

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1009, 685)
        font = QtGui.QFont()
        font.setBold(True)
        Dialog.setFont(font)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        Dialog.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("main_program/source/ui_design\\resources/pictures/icon.png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(420, 570, 181, 81))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setBold(True)
        font.setItalic(False)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {\n"
"  display: grid;\n"
"  place-items: center;\n"
"  background: #e3edf7;\n"
"  padding: 1.4em;\n"
"  border-radius: 10px;\n"
"  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.15),\n"
"          -6px -6px 10px -1px rgba(255,255,255,0.7);\n"
"  border: 1px solid rgba(0,0,0,0);\n"
"  cursor: pointer;\n"
"  transition: transform 0.5s;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  box-shadow: inset 4px 4px 6px -1px rgba(0,0,0,0.2),\n"
"          inset -4px -4px 6px -1px rgba(255,255,255,0.7),\n"
"          -0.5px -0.5px 0px rgba(255,255,255,1),\n"
"          0.5px 0.5px 0px rgba(0,0,0,0.15),\n"
"          0px 12px 10px -10px rgba(0,0,0,0.05);\n"
"  border: 1px solid rgba(0,0,0,0.1);\n"
"  transform: translateY(0.5em);\n"
"}\n"
"\n"
"QPushButton svg {\n"
"  transition: transform 0.5s;\n"
"}\n"
"\n"
"QPushButton:hover svg {\n"
"  transform: scale(0.9);\n"
"  fill: #333333;\n"
"}\n"
"\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("main_program/source/ui_design\\resources/pictures/pusbuttonicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(250, 470, 561, 31))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("QLineEdit{ border: 2px solid red; background-color: orange }\n"
"\n"
"QLineEdit:hover{\n"
"        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #ffd9aa,\n"
"                stop :   0.5 #ffbb6e, stop :   0.55 #feae42, stop :   1.0 #fedb74);\n"
"}\n"
"\n"
"QLineEdit {\n"
"        border: 1px solid #6593cf;\n"
"        border-radius: 2px;\n"
"        padding: 5px 15px 2px 5px;\n"
"        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #f5f9ff,\n"
"                stop :   0.5 #c7dfff, stop :   0.55 #afd2ff, stop :   1.0 #c0dbff);\n"
"        color: #006aff;\n"
"        font: bold large \"Arial\";\n"
"        height: 30px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QLineEdit:pressed {\n"
"        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #c0dbff,\n"
"        stop :   0.5 #cfd26f, stop :   0.55 #c7df6f, stop :   1.0 #f5f9ff);\n"
"        padding-top: 2px;\n"
"        padding-left: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit:on {\n"
"        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #5AA72D,\n"
"        stop :   0.5 #B3E296, stop :   0.55 #B3E296, stop :   1.0 #f5f9ff);\n"
"        padding-top: 2px;\n"
"        padding-left: 3px;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"        background: transparent #e5e9ee;\n"
"        padding-top: 2px;        \n"
"        padding-left: 3px;\n"
"        color: black;\n"
"}")
        self.lineEdit.setMaxLength(50)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalSlider = QtWidgets.QSlider(Dialog)
        self.horizontalSlider.setGeometry(QtCore.QRect(250, 510, 561, 31))
        self.horizontalSlider.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.horizontalSlider.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.horizontalSlider.setAcceptDrops(False)
        self.horizontalSlider.setAccessibleDescription("")
        self.horizontalSlider.setAutoFillBackground(False)
        self.horizontalSlider.setStyleSheet("QSlider{ border: 2px solid red; background-color: orange }\n"
"\n"
"QSlider:hover{\n"
"        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #ffd9aa,\n"
"                stop :   0.5 #ffbb6e, stop :   0.55 #feae42, stop :   1.0 #fedb74);\n"
"}\n"
"\n"
"QSlider {\n"
"        border: 1px solid #6593cf;\n"
"        border-radius: 2px;\n"
"        padding: 5px 15px 2px 5px;\n"
"        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #f5f9ff,\n"
"                stop :   0.5 #c7dfff, stop :   0.55 #afd2ff, stop :   1.0 #c0dbff);\n"
"        color: #006aff;\n"
"        font: bold large \"Arial\";\n"
"        height: 30px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QSlider:pressed {\n"
"        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #c0dbff,\n"
"        stop :   0.5 #cfd26f, stop :   0.55 #c7df6f, stop :   1.0 #f5f9ff);\n"
"        padding-top: 2px;\n"
"        padding-left: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider:on {\n"
"        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #5AA72D,\n"
"        stop :   0.5 #B3E296, stop :   0.55 #B3E296, stop :   1.0 #f5f9ff);\n"
"        padding-top: 2px;\n"
"        padding-left: 3px;\n"
"}\n"
"\n"
"QSlider:disabled {\n"
"        background: transparent #e5e9ee;\n"
"        padding-top: 2px;        \n"
"        padding-left: 3px;\n"
"        color: black;\n"
"}")
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setTracking(False)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(250, 160, 561, 301))
        self.graphicsView.setStyleSheet("QGraphicsView { border: 2px solid red; background-color: orange }\n"
"\n"
"QGraphicsView:hover{\n"
"        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #ffd9aa,\n"
"                stop :   0.5 #ffbb6e, stop :   0.55 #feae42, stop :   1.0 #fedb74);\n"
"}\n"
"\n"
"QGraphicsView {\n"
"        border: 1px solid #6593cf;\n"
"        border-radius: 2px;\n"
"        padding: 5px 15px 2px 5px;\n"
"        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #f5f9ff,\n"
"                stop :   0.5 #c7dfff, stop :   0.55 #afd2ff, stop :   1.0 #c0dbff);\n"
"        color: #006aff;\n"
"        font: bold large \"Arial\";\n"
"        height: 30px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QGraphicsView:pressed {\n"
"        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #c0dbff,\n"
"        stop :   0.5 #cfd26f, stop :   0.55 #c7df6f, stop :   1.0 #f5f9ff);\n"
"        padding-top: 2px;\n"
"        padding-left: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QGraphicsView:on {\n"
"        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #5AA72D,\n"
"        stop :   0.5 #B3E296, stop :   0.55 #B3E296, stop :   1.0 #f5f9ff);\n"
"        padding-top: 2px;\n"
"        padding-left: 3px;\n"
"}\n"
"\n"
"QGraphicsView:disabled {\n"
"        background: transparent #e5e9ee;\n"
"        padding-top: 2px;        \n"
"        padding-left: 3px;\n"
"        color: black;\n"
"}")
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 520, 101, 16))
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(250, 130, 601, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(830, 510, 64, 31))
        self.lcdNumber.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.lcdNumber.setDigitCount(99)
        self.lcdNumber.setMode(QtWidgets.QLCDNumber.Hex)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(280, 170, 501, 281))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        self.horizontalSlider.sliderMoved['int'].connect(self.lcdNumber.update) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "NyvoAI"))
        self.pushButton.setToolTip(_translate("Dialog", "<html><head/><body><p>Generate the image!</p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Dig IP"))
        self.lineEdit.setToolTip(_translate("Dialog", "<html><head/><body><p>Enter the prompt you would like the picture to be generated from</p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Enter your desired prompt here"))
        self.horizontalSlider.setToolTip(_translate("Dialog", "<html><head/><body><p>Choose how creative the AI can be while generating the prompt.</p><p>( The higher the prompt weight: Increased creativity )</p><p>( The lesser prompt weight: Increased prominent )</p></body></html>"))
        self.graphicsView.setToolTip(_translate("Dialog", "<html><head/><body><p>The generated image will be visible <span style=\" font-style:italic; text-decoration: underline;\">here</span>.</p></body></html>"))
        self.label.setText(_translate("Dialog", "Prompt Weight"))
        self.progressBar.setToolTip(_translate("Dialog", "<html><head/><body><p>Generating Image...</p></body></html>"))
        self.lcdNumber.setToolTip(_translate("Dialog", "<html><head/><body><p>Prompt weight in percentage</p></body></html>"))


class NyvoaiApp(QDialog):

    def make_api_call(self, ip: str) -> str:
    
        api_url = "https://api.api-ninjas.com/v1/iplookup?address="
        api_key = {
            "X-Api-Key" : "mWNfs+SWsyZk+Wx6r5AyGw==cFD5QGOQyTJo3Xzb", # ! HAVE FUN WITH THE API KEY LADS!
            
        }
        
    
        if not isinstance(ip, str):
            raise ValueError("Invalid argument type passed for the parameter prompt | Expected: (str) |")
            
    
        response = requests.get(url=f"{api_url}{ip}", headers=api_key)
        return response.text
    
    
    def show_lineedit_result(self):
    
        self.ui.label_2.setText(self.make_api_call(self.ui.lineEdit.text()))

    def __init__(self):

        super().__init__()
        self.ui = Ui_Dialog()

        self.ui.setupUi(self)
        self.api_image = None
        
        self.ui.pushButton.clicked.connect(self.show_lineedit_result)
        
        self.show()

        
if __name__ == "__main__":


    app = QApplication(sys.argv)
    app_window = NyvoaiApp()

   
    app_window.show()
    sys.exit(app_window.exec_())