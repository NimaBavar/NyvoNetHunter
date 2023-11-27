#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# NyvoNetHunter main module.
BY: NyvoStudio, KhodeNima ( Nima Bavar )
---
# This project and all of its components are licensed under the AGPL-3.0 ( GNU Affero Public License v3.0 ) license agreements.
"""


from database.packages import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(898, 685)
        font = QtGui.QFont()
        font.setBold(True)
        Dialog.setFont(font)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        Dialog.setMouseTracking(False)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(430, 530, 211, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setItalic(False)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton.setWhatsThis("")
        self.pushButton.setStyleSheet(
            "QPushButton{ border: 2px solid red; background-color: orange }\n"
            "\n"
            "QPushButton:hover{\n"
            "        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #ffd9aa,\n"
            "                stop :   0.5 #ffbb6e, stop :   0.55 #feae42, stop :   1.0 #fedb74);\n"
            "}\n"
            "\n"
            "QPushButton {\n"
            "        border: 1px solid #6593cf;\n"
            "        border-radius: 2px;\n"
            "        padding: 5px 15px 2px 5px;\n"
            "        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #f5f9ff,\n"
            "                stop :   0.5 #c7dfff, stop :   0.55 #afd2ff, stop :   1.0 #c0dbff);\n"
            "        color: #006aff;\n"
            '        font: bold large "Arial";\n'
            "        height: 30px;\n"
            "}\n"
            "\n"
            "\n"
            "\n"
            "\n"
            "QPushButton:pressed {\n"
            "        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #c0dbff,\n"
            "        stop :   0.5 #cfd26f, stop :   0.55 #c7df6f, stop :   1.0 #f5f9ff);\n"
            "        padding-top: 2px;\n"
            "        padding-left: 3px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton:on {\n"
            "        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #5AA72D,\n"
            "        stop :   0.5 #B3E296, stop :   0.55 #B3E296, stop :   1.0 #f5f9ff);\n"
            "        padding-top: 2px;\n"
            "        padding-left: 3px;\n"
            "}\n"
            "\n"
            "QPushButton:disabled {\n"
            "        background: transparent #e5e9ee;\n"
            "        padding-top: 2px;        \n"
            "        padding-left: 3px;\n"
            "        color: black;\n"
            "}\n"
            ""
        )
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(
                "main_program/source/ui_design/resources/pictures/pushbuttonicon.png"
            ),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(35, 35))
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(250, 490, 561, 31))
        self.lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet(
            "QLineEdit{ border: 2px solid red; background-color: orange }\n"
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
            '        font: bold large "Arial";\n'
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
            "}"
        )
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhSensitiveData)
        self.lineEdit.setMaxLength(50)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(250, 180, 561, 301))
        self.graphicsView.setFocusPolicy(QtCore.Qt.NoFocus)
        self.graphicsView.setStyleSheet(
            "QGraphicsView { border: 2px solid red; background-color: orange }\n"
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
            '        font: bold large "Arial";\n'
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
            "}"
        )
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(480, 100, 121, 31))
        self.label.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.label.setStyleSheet(
            "QLabel{ border: 2px solid red; background-color: orange }\n"
            "\n"
            "QLabel:hover{\n"
            "        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #ffd9aa,\n"
            "                stop :   0.5 #ffbb6e, stop :   0.55 #feae42, stop :   1.0 #fedb74);\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "        border: 1px solid #6593cf;\n"
            "        border-radius: 2px;\n"
            "        padding: 5px 15px 2px 5px;\n"
            "        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #f5f9ff,\n"
            "                stop :   0.5 #c7dfff, stop :   0.55 #afd2ff, stop :   1.0 #c0dbff);\n"
            "        color: #006aff;\n"
            '        font: bold large "Arial";\n'
            "        height: 30px;\n"
            "}\n"
            "\n"
            "\n"
            "\n"
            "\n"
            "QLabel:pressed {\n"
            "        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #c0dbff,\n"
            "        stop :   0.5 #cfd26f, stop :   0.55 #c7df6f, stop :   1.0 #f5f9ff);\n"
            "        padding-top: 2px;\n"
            "        padding-left: 3px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QLabel:on {\n"
            "        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #5AA72D,\n"
            "        stop :   0.5 #B3E296, stop :   0.55 #B3E296, stop :   1.0 #f5f9ff);\n"
            "        padding-top: 2px;\n"
            "        padding-left: 3px;\n"
            "}\n"
            "\n"
            "QLabel:disabled {\n"
            "        background: transparent #e5e9ee;\n"
            "        padding-top: 2px;        \n"
            "        padding-left: 3px;\n"
            "        color: black;\n"
            "}"
        )
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(250, 140, 561, 31))
        self.progressBar.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.progressBar.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.progressBar.setStyleSheet(
            "QProgressBar {\n"
            "\n"
            "\n"
            "    border:2px solid red;  \n"
            "    border-radius:5px; \n"
            "    text-align:center;\n"
            "\n"
            "\n"
            "}\n"
            " \n"
            "\n"
            "QProgressBar::chunk {\n"
            "\n"
            "    background-color:#05B8CC;\n"
            "    width:5px; \n"
            "    margin:1px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QProgressBar{ border: 2px solid red; background-color: orange }\n"
            "\n"
            "QProgressBar:hover{\n"
            "        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #ffd9aa,\n"
            "                stop :   0.5 #ffbb6e, stop :   0.55 #feae42, stop :   1.0 #fedb74);\n"
            "}\n"
            "\n"
            "QProgressBar {\n"
            "        border: 1px solid #6593cf;\n"
            "        border-radius: 2px;\n"
            "        padding: 5px 15px 2px 5px;\n"
            "        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #f5f9ff,\n"
            "                stop :   0.5 #c7dfff, stop :   0.55 #afd2ff, stop :   1.0 #c0dbff);\n"
            "        color: #006aff;\n"
            '        font: bold large "Arial";\n'
            "        height: 30px;\n"
            "}\n"
            "\n"
            "\n"
            "\n"
            "\n"
            "QProgressBar:pressed {\n"
            "        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #c0dbff,\n"
            "        stop :   0.5 #cfd26f, stop :   0.55 #c7df6f, stop :   1.0 #f5f9ff);\n"
            "        padding-top: 2px;\n"
            "        padding-left: 3px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QProgressBar:on {\n"
            "        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #5AA72D,\n"
            "        stop :   0.5 #B3E296, stop :   0.55 #B3E296, stop :   1.0 #f5f9ff);\n"
            "        padding-top: 2px;\n"
            "        padding-left: 3px;\n"
            "}\n"
            "\n"
            "QProgressBar:disabled {\n"
            "        background: transparent #e5e9ee;\n"
            "        padding-top: 2px;        \n"
            "        padding-left: 3px;\n"
            "        color: black;\n"
            "}\n"
            "\n"
            "\n"
            ""
        )
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(280, 190, 501, 281))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.graphicsView_2 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_2.setGeometry(QtCore.QRect(70, 180, 171, 301))
        self.graphicsView_2.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.graphicsView_2.setStyleSheet(
            "QGraphicsView { border: 2px solid red; background-color: orange }\n"
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
            '        font: bold large "Arial";\n'
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
            "}"
        )
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(80, 200, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.checkBox.setFont(font)
        self.checkBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.checkBox.setStyleSheet(
            "QCheckBox {\n"
            "  width: 35px;\n"
            "  height: 35px;\n"
            "  cursor: pointer;\n"
            "  margin-right: -22px;\n"
            "  appearance: none;\n"
            "  border-radius: 5px;\n"
            "  background-color: #6593cf;\n"
            "  z-index: 2;\n"
            "  transition: all 0.3s;\n"
            "}\n"
            "\n"
            ".container {\n"
            "  width: 35px;\n"
            "  height: 35px;\n"
            "  position: relative;\n"
            "  top: 4px;\n"
            "  left: -8%;\n"
            "  border-radius: 5px;\n"
            "  background-color: #6593cf;\n"
            "  transition: all 0.3s;\n"
            "}\n"
            "\n"
            "QCheckBox::before {\n"
            '  content: "";\n'
            "  background-color: #6593cf;\n"
            "  position: relative;\n"
            "  display: flex;\n"
            "  top: 45%;\n"
            "  left: 50%;\n"
            "  width: 55px;\n"
            "  height: 3px;\n"
            "  border-radius: 25px;\n"
            "  transform: translate(100px, 0px) scale(0);\n"
            "  transition: ease-out 0.15s;\n"
            "}\n"
            "\n"
            "QCheckBox:checked::before {\n"
            "  transform: translateX(2em);\n"
            "  top: 12px;\n"
            "  transition: ease-out 0.15s;\n"
            "}\n"
            "\n"
            "QcheckBox:hover {\n"
            "  transform: translate(4px, 4px);\n"
            "  transition: ease-out 0.15s;\n"
            "  background-color: #6593cf;\n"
            "}\n"
            "\n"
            "QCheckBox:checked {\n"
            "  transform: translate(4px, 4px);\n"
            "  transition: ease-out 0.15s;\n"
            "  background-color: #6593cf;\n"
            "}\n"
            "\n"
            ".svg-icon {\n"
            "  position: absolute;\n"
            "  width: 25px;\n"
            "  height: 25px;\n"
            "  display: flex;\n"
            "  z-index: 3;\n"
            "  top: 35%;\n"
            "  left: 11%;\n"
            "  color: #fefefe;\n"
            '  font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;\n'
            "  transform: rotate(0deg) scale(0);\n"
            "  transition: ease-in 0.2s;\n"
            "}\n"
            "\n"
            "QCheckBoxchecked ~ .svg-icon {\n"
            "  transform: rotate(360deg) scale(1);\n"
            "  transition: ease-in 0.2s;\n"
            "}\n"
            ""
        )
        self.checkBox.setObjectName("checkBox")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 140, 171, 31))
        self.label_3.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.label_3.setStyleSheet(
            "QLabel{ border: 2px solid red; background-color: orange }\n"
            "\n"
            "QLabel:hover{\n"
            "        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #ffd9aa,\n"
            "                stop :   0.5 #ffbb6e, stop :   0.55 #feae42, stop :   1.0 #fedb74);\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "        border: 1px solid #6593cf;\n"
            "        border-radius: 2px;\n"
            "        padding: 5px 15px 2px 5px;\n"
            "        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #f5f9ff,\n"
            "                stop :   0.5 #c7dfff, stop :   0.55 #afd2ff, stop :   1.0 #c0dbff);\n"
            "        color: #006aff;\n"
            '        font: bold large "Arial";\n'
            "        height: 30px;\n"
            "}\n"
            "\n"
            "\n"
            "\n"
            "\n"
            "QLabel:pressed {\n"
            "        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #c0dbff,\n"
            "        stop :   0.5 #cfd26f, stop :   0.55 #c7df6f, stop :   1.0 #f5f9ff);\n"
            "        padding-top: 2px;\n"
            "        padding-left: 3px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QLabel:on {\n"
            "        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #5AA72D,\n"
            "        stop :   0.5 #B3E296, stop :   0.55 #B3E296, stop :   1.0 #f5f9ff);\n"
            "        padding-top: 2px;\n"
            "        padding-left: 3px;\n"
            "}\n"
            "\n"
            "QLabel:disabled {\n"
            "        background: transparent #e5e9ee;\n"
            "        padding-top: 2px;        \n"
            "        padding-left: 3px;\n"
            "        color: black;\n"
            "}"
        )
        self.label_3.setObjectName("label_3")
        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(80, 220, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_2.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.checkBox_2.setStyleSheet(
            "QCheckBox {\n"
            "  width: 35px;\n"
            "  height: 35px;\n"
            "  cursor: pointer;\n"
            "  margin-right: -22px;\n"
            "  appearance: none;\n"
            "  border-radius: 5px;\n"
            "  background-color: #6593cf;\n"
            "  z-index: 2;\n"
            "  transition: all 0.3s;\n"
            "}\n"
            "\n"
            ".container {\n"
            "  width: 35px;\n"
            "  height: 35px;\n"
            "  position: relative;\n"
            "  top: 4px;\n"
            "  left: -8%;\n"
            "  border-radius: 5px;\n"
            "  background-color: #6593cf;\n"
            "  transition: all 0.3s;\n"
            "}\n"
            "\n"
            "QCheckBox::before {\n"
            '  content: "";\n'
            "  background-color: #6593cf;\n"
            "  position: relative;\n"
            "  display: flex;\n"
            "  top: 45%;\n"
            "  left: 50%;\n"
            "  width: 55px;\n"
            "  height: 3px;\n"
            "  border-radius: 25px;\n"
            "  transform: translate(100px, 0px) scale(0);\n"
            "  transition: ease-out 0.15s;\n"
            "}\n"
            "\n"
            "QCheckBox:checked::before {\n"
            "  transform: translateX(2em);\n"
            "  top: 12px;\n"
            "  transition: ease-out 0.15s;\n"
            "}\n"
            "\n"
            "QcheckBox:hover {\n"
            "  transform: translate(4px, 4px);\n"
            "  transition: ease-out 0.15s;\n"
            "  background-color: #6593cf;\n"
            "}\n"
            "\n"
            "QCheckBox:checked {\n"
            "  transform: translate(4px, 4px);\n"
            "  transition: ease-out 0.15s;\n"
            "  background-color: #6593cf;\n"
            "}\n"
            "\n"
            ".svg-icon {\n"
            "  position: absolute;\n"
            "  width: 25px;\n"
            "  height: 25px;\n"
            "  display: flex;\n"
            "  z-index: 3;\n"
            "  top: 35%;\n"
            "  left: 11%;\n"
            "  color: #fefefe;\n"
            '  font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;\n'
            "  transform: rotate(0deg) scale(0);\n"
            "  transition: ease-in 0.2s;\n"
            "}\n"
            "\n"
            "QCheckBoxchecked ~ .svg-icon {\n"
            "  transform: rotate(360deg) scale(1);\n"
            "  transition: ease-in 0.2s;\n"
            "}\n"
            ""
        )
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_3.setGeometry(QtCore.QRect(80, 240, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_3.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.checkBox_3.setStyleSheet(
            "QCheckBox {\n"
            "  width: 35px;\n"
            "  height: 35px;\n"
            "  cursor: pointer;\n"
            "  margin-right: -22px;\n"
            "  appearance: none;\n"
            "  border-radius: 5px;\n"
            "  background-color: #6593cf;\n"
            "  z-index: 2;\n"
            "  transition: all 0.3s;\n"
            "}\n"
            "\n"
            ".container {\n"
            "  width: 35px;\n"
            "  height: 35px;\n"
            "  position: relative;\n"
            "  top: 4px;\n"
            "  left: -8%;\n"
            "  border-radius: 5px;\n"
            "  background-color: #6593cf;\n"
            "  transition: all 0.3s;\n"
            "}\n"
            "\n"
            "QCheckBox::before {\n"
            '  content: "";\n'
            "  background-color: #6593cf;\n"
            "  position: relative;\n"
            "  display: flex;\n"
            "  top: 45%;\n"
            "  left: 50%;\n"
            "  width: 55px;\n"
            "  height: 3px;\n"
            "  border-radius: 25px;\n"
            "  transform: translate(100px, 0px) scale(0);\n"
            "  transition: ease-out 0.15s;\n"
            "}\n"
            "\n"
            "QCheckBox:checked::before {\n"
            "  transform: translateX(2em);\n"
            "  top: 12px;\n"
            "  transition: ease-out 0.15s;\n"
            "}\n"
            "\n"
            "QcheckBox:hover {\n"
            "  transform: translate(4px, 4px);\n"
            "  transition: ease-out 0.15s;\n"
            "  background-color: #6593cf;\n"
            "}\n"
            "\n"
            "QCheckBox:checked {\n"
            "  transform: translate(4px, 4px);\n"
            "  transition: ease-out 0.15s;\n"
            "  background-color: #6593cf;\n"
            "}\n"
            "\n"
            ".svg-icon {\n"
            "  position: absolute;\n"
            "  width: 25px;\n"
            "  height: 25px;\n"
            "  display: flex;\n"
            "  z-index: 3;\n"
            "  top: 35%;\n"
            "  left: 11%;\n"
            "  color: #fefefe;\n"
            '  font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;\n'
            "  transform: rotate(0deg) scale(0);\n"
            "  transition: ease-in 0.2s;\n"
            "}\n"
            "\n"
            "QCheckBoxchecked ~ .svg-icon {\n"
            "  transform: rotate(360deg) scale(1);\n"
            "  transition: ease-in 0.2s;\n"
            "}\n"
            ""
        )
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_4.setGeometry(QtCore.QRect(80, 260, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_4.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.checkBox_4.setStyleSheet(
            "QCheckBox {\n"
            "  width: 35px;\n"
            "  height: 35px;\n"
            "  cursor: pointer;\n"
            "  margin-right: -22px;\n"
            "  appearance: none;\n"
            "  border-radius: 5px;\n"
            "  background-color: #6593cf;\n"
            "  z-index: 2;\n"
            "  transition: all 0.3s;\n"
            "}\n"
            "\n"
            ".container {\n"
            "  width: 35px;\n"
            "  height: 35px;\n"
            "  position: relative;\n"
            "  top: 4px;\n"
            "  left: -8%;\n"
            "  border-radius: 5px;\n"
            "  background-color: #6593cf;\n"
            "  transition: all 0.3s;\n"
            "}\n"
            "\n"
            "QCheckBox::before {\n"
            '  content: "";\n'
            "  background-color: #6593cf;\n"
            "  position: relative;\n"
            "  display: flex;\n"
            "  top: 45%;\n"
            "  left: 50%;\n"
            "  width: 55px;\n"
            "  height: 3px;\n"
            "  border-radius: 25px;\n"
            "  transform: translate(100px, 0px) scale(0);\n"
            "  transition: ease-out 0.15s;\n"
            "}\n"
            "\n"
            "QCheckBox:checked::before {\n"
            "  transform: translateX(2em);\n"
            "  top: 12px;\n"
            "  transition: ease-out 0.15s;\n"
            "}\n"
            "\n"
            "QcheckBox:hover {\n"
            "  transform: translate(4px, 4px);\n"
            "  transition: ease-out 0.15s;\n"
            "  background-color: #6593cf;\n"
            "}\n"
            "\n"
            "QCheckBox:checked {\n"
            "  transform: translate(4px, 4px);\n"
            "  transition: ease-out 0.15s;\n"
            "  background-color: #6593cf;\n"
            "}\n"
            "\n"
            ".svg-icon {\n"
            "  position: absolute;\n"
            "  width: 25px;\n"
            "  height: 25px;\n"
            "  display: flex;\n"
            "  z-index: 3;\n"
            "  top: 35%;\n"
            "  left: 11%;\n"
            "  color: #fefefe;\n"
            '  font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;\n'
            "  transform: rotate(0deg) scale(0);\n"
            "  transition: ease-in 0.2s;\n"
            "}\n"
            "\n"
            "QCheckBoxchecked ~ .svg-icon {\n"
            "  transform: rotate(360deg) scale(1);\n"
            "  transition: ease-in 0.2s;\n"
            "}\n"
            ""
        )
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_5.setGeometry(QtCore.QRect(80, 280, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_5.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.checkBox_5.setStyleSheet(
            "QCheckBox {\n"
            "  width: 35px;\n"
            "  height: 35px;\n"
            "  cursor: pointer;\n"
            "  margin-right: -22px;\n"
            "  appearance: none;\n"
            "  border-radius: 5px;\n"
            "  background-color: #6593cf;\n"
            "  z-index: 2;\n"
            "  transition: all 0.3s;\n"
            "}\n"
            "\n"
            ".container {\n"
            "  width: 35px;\n"
            "  height: 35px;\n"
            "  position: relative;\n"
            "  top: 4px;\n"
            "  left: -8%;\n"
            "  border-radius: 5px;\n"
            "  background-color: #6593cf;\n"
            "  transition: all 0.3s;\n"
            "}\n"
            "\n"
            "QCheckBox::before {\n"
            '  content: "";\n'
            "  background-color: #6593cf;\n"
            "  position: relative;\n"
            "  display: flex;\n"
            "  top: 45%;\n"
            "  left: 50%;\n"
            "  width: 55px;\n"
            "  height: 3px;\n"
            "  border-radius: 25px;\n"
            "  transform: translate(100px, 0px) scale(0);\n"
            "  transition: ease-out 0.15s;\n"
            "}\n"
            "\n"
            "QCheckBox:checked::before {\n"
            "  transform: translateX(2em);\n"
            "  top: 12px;\n"
            "  transition: ease-out 0.15s;\n"
            "}\n"
            "\n"
            "QcheckBox:hover {\n"
            "  transform: translate(4px, 4px);\n"
            "  transition: ease-out 0.15s;\n"
            "  background-color: #6593cf;\n"
            "}\n"
            "\n"
            "QCheckBox:checked {\n"
            "  transform: translate(4px, 4px);\n"
            "  transition: ease-out 0.15s;\n"
            "  background-color: #6593cf;\n"
            "}\n"
            "\n"
            ".svg-icon {\n"
            "  position: absolute;\n"
            "  width: 25px;\n"
            "  height: 25px;\n"
            "  display: flex;\n"
            "  z-index: 3;\n"
            "  top: 35%;\n"
            "  left: 11%;\n"
            "  color: #fefefe;\n"
            '  font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;\n'
            "  transform: rotate(0deg) scale(0);\n"
            "  transition: ease-in 0.2s;\n"
            "}\n"
            "\n"
            "QCheckBoxchecked ~ .svg-icon {\n"
            "  transform: rotate(360deg) scale(1);\n"
            "  transition: ease-in 0.2s;\n"
            "}\n"
            ""
        )
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_6.setGeometry(QtCore.QRect(80, 300, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_6.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.checkBox_6.setStyleSheet(
            "QCheckBox {\n"
            "  width: 35px;\n"
            "  height: 35px;\n"
            "  cursor: pointer;\n"
            "  margin-right: -22px;\n"
            "  appearance: none;\n"
            "  border-radius: 5px;\n"
            "  background-color: #6593cf;\n"
            "  z-index: 2;\n"
            "  transition: all 0.3s;\n"
            "}\n"
            "\n"
            ".container {\n"
            "  width: 35px;\n"
            "  height: 35px;\n"
            "  position: relative;\n"
            "  top: 4px;\n"
            "  left: -8%;\n"
            "  border-radius: 5px;\n"
            "  background-color: #6593cf;\n"
            "  transition: all 0.3s;\n"
            "}\n"
            "\n"
            "QCheckBox::before {\n"
            '  content: "";\n'
            "  background-color: #6593cf;\n"
            "  position: relative;\n"
            "  display: flex;\n"
            "  top: 45%;\n"
            "  left: 50%;\n"
            "  width: 55px;\n"
            "  height: 3px;\n"
            "  border-radius: 25px;\n"
            "  transform: translate(100px, 0px) scale(0);\n"
            "  transition: ease-out 0.15s;\n"
            "}\n"
            "\n"
            "QCheckBox:checked::before {\n"
            "  transform: translateX(2em);\n"
            "  top: 12px;\n"
            "  transition: ease-out 0.15s;\n"
            "}\n"
            "\n"
            "QcheckBox:hover {\n"
            "  transform: translate(4px, 4px);\n"
            "  transition: ease-out 0.15s;\n"
            "  background-color: #6593cf;\n"
            "}\n"
            "\n"
            "QCheckBox:checked {\n"
            "  transform: translate(4px, 4px);\n"
            "  transition: ease-out 0.15s;\n"
            "  background-color: #6593cf;\n"
            "}\n"
            "\n"
            ".svg-icon {\n"
            "  position: absolute;\n"
            "  width: 25px;\n"
            "  height: 25px;\n"
            "  display: flex;\n"
            "  z-index: 3;\n"
            "  top: 35%;\n"
            "  left: 11%;\n"
            "  color: #fefefe;\n"
            '  font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;\n'
            "  transform: rotate(0deg) scale(0);\n"
            "  transition: ease-in 0.2s;\n"
            "}\n"
            "\n"
            "QCheckBoxchecked ~ .svg-icon {\n"
            "  transform: rotate(360deg) scale(1);\n"
            "  transition: ease-in 0.2s;\n"
            "}\n"
            ""
        )
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_7.setGeometry(QtCore.QRect(80, 430, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_7.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.checkBox_7.setStyleSheet(
            "QCheckBox {\n"
            "  width: 35px;\n"
            "  height: 35px;\n"
            "  cursor: pointer;\n"
            "  margin-right: -22px;\n"
            "  appearance: none;\n"
            "  border-radius: 5px;\n"
            "  background-color: #FF0000;\n"
            "  z-index: 2;\n"
            "  transition: all 0.3s;\n"
            "}\n"
            "\n"
            ".container {\n"
            "  width: 35px;\n"
            "  height: 35px;\n"
            "  position: relative;\n"
            "  top: 4px;\n"
            "  left: -8%;\n"
            "  border-radius: 5px;\n"
            "  background-color: #FF0000;\n"
            "  transition: all 0.3s;\n"
            "}\n"
            "\n"
            "QCheckBox::before {\n"
            '  content: "";\n'
            "  background-color: #FF0000;\n"
            "  position: relative;\n"
            "  display: flex;\n"
            "  top: 45%;\n"
            "  left: 50%;\n"
            "  width: 55px;\n"
            "  height: 3px;\n"
            "  border-radius: 25px;\n"
            "  transform: translate(100px, 0px) scale(0);\n"
            "  transition: ease-out 0.15s;\n"
            "}\n"
            "\n"
            "QCheckBox:checked::before {\n"
            "  transform: translateX(2em);\n"
            "  top: 12px;\n"
            "  transition: ease-out 0.15s;\n"
            "}\n"
            "\n"
            "QcheckBox:hover {\n"
            "  transform: translate(4px, 4px);\n"
            "  transition: ease-out 0.15s;\n"
            "  background-color: #FF0000;\n"
            "}\n"
            "\n"
            "QCheckBox:checked {\n"
            "  transform: translate(4px, 4px);\n"
            "  transition: ease-out 0.15s;\n"
            "  background-color: #FF0000;\n"
            "}\n"
            "\n"
            ".svg-icon {\n"
            "  position: absolute;\n"
            "  width: 25px;\n"
            "  height: 25px;\n"
            "  display: flex;\n"
            "  z-index: 3;\n"
            "  top: 35%;\n"
            "  left: 11%;\n"
            "  color: #fefefe;\n"
            '  font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;\n'
            "  transform: rotate(0deg) scale(0);\n"
            "  transition: ease-in 0.2s;\n"
            "}\n"
            "\n"
            "QCheckBoxchecked ~ .svg-icon {\n"
            "  transform: rotate(360deg) scale(1);\n"
            "  transition: ease-in 0.2s;\n"
            "}\n"
            ""
        )
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_8.setGeometry(QtCore.QRect(80, 330, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_8.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.checkBox_8.setStyleSheet(
            "QCheckBox {\n"
            "  width: 35px;\n"
            "  height: 35px;\n"
            "  cursor: pointer;\n"
            "  margin-right: -22px;\n"
            "  appearance: none;\n"
            "  border-radius: 5px;\n"
            "  background-color: #6593cf;\n"
            "  z-index: 2;\n"
            "  transition: all 0.3s;\n"
            "}\n"
            "\n"
            ".container {\n"
            "  width: 35px;\n"
            "  height: 35px;\n"
            "  position: relative;\n"
            "  top: 4px;\n"
            "  left: -8%;\n"
            "  border-radius: 5px;\n"
            "  background-color: #6593cf;\n"
            "  transition: all 0.3s;\n"
            "}\n"
            "\n"
            "QCheckBox::before {\n"
            '  content: "";\n'
            "  background-color: #6593cf;\n"
            "  position: relative;\n"
            "  display: flex;\n"
            "  top: 45%;\n"
            "  left: 50%;\n"
            "  width: 55px;\n"
            "  height: 3px;\n"
            "  border-radius: 25px;\n"
            "  transform: translate(100px, 0px) scale(0);\n"
            "  transition: ease-out 0.15s;\n"
            "}\n"
            "\n"
            "QCheckBox:checked::before {\n"
            "  transform: translateX(2em);\n"
            "  top: 12px;\n"
            "  transition: ease-out 0.15s;\n"
            "}\n"
            "\n"
            "QcheckBox:hover {\n"
            "  transform: translate(4px, 4px);\n"
            "  transition: ease-out 0.15s;\n"
            "  background-color: #6593cf;\n"
            "}\n"
            "\n"
            "QCheckBox:checked {\n"
            "  transform: translate(4px, 4px);\n"
            "  transition: ease-out 0.15s;\n"
            "  background-color: #6593cf;\n"
            "}\n"
            "\n"
            ".svg-icon {\n"
            "  position: absolute;\n"
            "  width: 25px;\n"
            "  height: 25px;\n"
            "  display: flex;\n"
            "  z-index: 3;\n"
            "  top: 35%;\n"
            "  left: 11%;\n"
            "  color: #fefefe;\n"
            '  font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;\n'
            "  transform: rotate(0deg) scale(0);\n"
            "  transition: ease-in 0.2s;\n"
            "}\n"
            "\n"
            "QCheckBoxchecked ~ .svg-icon {\n"
            "  transform: rotate(360deg) scale(1);\n"
            "  transition: ease-in 0.2s;\n"
            "}\n"
            ""
        )
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_9.setGeometry(QtCore.QRect(80, 350, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.checkBox_9.setFont(font)
        self.checkBox_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_9.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.checkBox_9.setStyleSheet(
            "QCheckBox {\n"
            "  width: 35px;\n"
            "  height: 35px;\n"
            "  cursor: pointer;\n"
            "  margin-right: -22px;\n"
            "  appearance: none;\n"
            "  border-radius: 5px;\n"
            "  background-color: #6593cf;\n"
            "  z-index: 2;\n"
            "  transition: all 0.3s;\n"
            "}\n"
            "\n"
            ".container {\n"
            "  width: 35px;\n"
            "  height: 35px;\n"
            "  position: relative;\n"
            "  top: 4px;\n"
            "  left: -8%;\n"
            "  border-radius: 5px;\n"
            "  background-color: #6593cf;\n"
            "  transition: all 0.3s;\n"
            "}\n"
            "\n"
            "QCheckBox::before {\n"
            '  content: "";\n'
            "  background-color: #6593cf;\n"
            "  position: relative;\n"
            "  display: flex;\n"
            "  top: 45%;\n"
            "  left: 50%;\n"
            "  width: 55px;\n"
            "  height: 3px;\n"
            "  border-radius: 25px;\n"
            "  transform: translate(100px, 0px) scale(0);\n"
            "  transition: ease-out 0.15s;\n"
            "}\n"
            "\n"
            "QCheckBox:checked::before {\n"
            "  transform: translateX(2em);\n"
            "  top: 12px;\n"
            "  transition: ease-out 0.15s;\n"
            "}\n"
            "\n"
            "QcheckBox:hover {\n"
            "  transform: translate(4px, 4px);\n"
            "  transition: ease-out 0.15s;\n"
            "  background-color: #6593cf;\n"
            "}\n"
            "\n"
            "QCheckBox:checked {\n"
            "  transform: translate(4px, 4px);\n"
            "  transition: ease-out 0.15s;\n"
            "  background-color: #6593cf;\n"
            "}\n"
            "\n"
            ".svg-icon {\n"
            "  position: absolute;\n"
            "  width: 25px;\n"
            "  height: 25px;\n"
            "  display: flex;\n"
            "  z-index: 3;\n"
            "  top: 35%;\n"
            "  left: 11%;\n"
            "  color: #fefefe;\n"
            '  font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;\n'
            "  transform: rotate(0deg) scale(0);\n"
            "  transition: ease-in 0.2s;\n"
            "}\n"
            "\n"
            "QCheckBoxchecked ~ .svg-icon {\n"
            "  transform: rotate(360deg) scale(1);\n"
            "  transition: ease-in 0.2s;\n"
            "}\n"
            ""
        )
        self.checkBox_9.setObjectName("checkBox_9")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(70, 10, 171, 31))
        self.label_4.setStyleSheet(
            "QLabel{ border: 2px solid red; background-color: orange }\n"
            "\n"
            "QLabel:hover{\n"
            "        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #ffd9aa,\n"
            "                stop :   0.5 #ffbb6e, stop :   0.55 #feae42, stop :   1.0 #fedb74);\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "        border: 1px solid #6593cf;\n"
            "        border-radius: 2px;\n"
            "        padding: 5px 15px 2px 5px;\n"
            "        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #f5f9ff,\n"
            "                stop :   0.5 #c7dfff, stop :   0.55 #afd2ff, stop :   1.0 #c0dbff);\n"
            "        color: #006aff;\n"
            '        font: bold large "Arial";\n'
            "        height: 30px;\n"
            "}\n"
            "\n"
            "\n"
            "\n"
            "\n"
            "QLabel:pressed {\n"
            "        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #c0dbff,\n"
            "        stop :   0.5 #cfd26f, stop :   0.55 #c7df6f, stop :   1.0 #f5f9ff);\n"
            "        padding-top: 2px;\n"
            "        padding-left: 3px;\n"
            "\n"
            "}\n"
            "\n"
            "\n"
            "QLabel:on {\n"
            "        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #5AA72D,\n"
            "        stop :   0.5 #B3E296, stop :   0.55 #B3E296, stop :   1.0 #f5f9ff);\n"
            "        padding-top: 2px;\n"
            "        padding-left: 3px;\n"
            "}\n"
            "\n"
            "QLabel:disabled {\n"
            "        background: transparent #e5e9ee;\n"
            "        padding-top: 2px;        \n"
            "        padding-left: 3px;\n"
            "        color: black;\n"
            "}"
        )
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(88, 60, 141, 71))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "NyvoNetHunter"))
        self.pushButton.setToolTip(
            _translate(
                "Dialog", "<html><head/><body><p>Examine the IP!</p></body></html>"
            )
        )
        self.pushButton.setText(_translate("Dialog", "Examine"))
        self.lineEdit.setToolTip(
            _translate(
                "Dialog",
                "<html><head/><body><p>IP example: 144.145.146.147 ( IP addresses maximum octet digit is 255 )</p></body></html>",
            )
        )
        self.lineEdit.setPlaceholderText(
            _translate("Dialog", "Enter your desired IP or URL to examine: ")
        )
        self.graphicsView.setToolTip(
            _translate(
                "Dialog",
                '<html><head/><body><p>The examine operation outputs will be shown <span style=" font-style:italic; text-decoration: underline;">here.</span></p></body></html>',
            )
        )
        self.label.setText(_translate("Dialog", "Awaiting input..."))
        self.progressBar.setToolTip(
            _translate("Dialog", "<html><head/><body><p>Examining...</p></body></html>")
        )
        self.graphicsView_2.setToolTip(
            _translate(
                "Dialog",
                '<html><head/><body><p>The examine operation outputs will be shown <span style=" font-style:italic; text-decoration: underline;">here.</span></p></body></html>',
            )
        )
        self.checkBox.setText(_translate("Dialog", "Country"))
        self.label_3.setText(_translate("Dialog", "Examine options"))
        self.checkBox_2.setText(_translate("Dialog", "Region"))
        self.checkBox_3.setText(_translate("Dialog", "City"))
        self.checkBox_4.setText(_translate("Dialog", "Zip code"))
        self.checkBox_5.setText(_translate("Dialog", "Time zone"))
        self.checkBox_6.setToolTip(
            _translate(
                "Dialog",
                "<html><head/><body><p>The IP user Internet Service Provider.</p><p><br/></p><p>Examples: Mobin Net Communication Company, SURFnet II c.</p></body></html>",
            )
        )
        self.checkBox_6.setText(_translate("Dialog", "ISP"))
        self.checkBox_7.setToolTip(
            _translate(
                "Dialog",
                "<html><head/><body><p>The IP user Internet Service Provider.</p><p><br/></p><p>Examples: Mobin Net Communication Company, SURFnet II c.</p></body></html>",
            )
        )
        self.checkBox_7.setText(_translate("Dialog", "Show map location"))
        self.checkBox_8.setToolTip(
            _translate(
                "Dialog",
                "<html><head/><body><p>The IP user Internet Service Provider.</p><p><br/></p><p>Examples: Mobin Net Communication Company, SURFnet II c.</p></body></html>",
            )
        )
        self.checkBox_8.setText(_translate("Dialog", "latitude"))
        self.checkBox_9.setToolTip(
            _translate(
                "Dialog",
                "<html><head/><body><p>The IP user Internet Service Provider.</p><p><br/></p><p>Examples: Mobin Net Communication Company, SURFnet II c.</p></body></html>",
            )
        )
        self.checkBox_9.setText(_translate("Dialog", "Longitude"))
        self.label_4.setText(_translate("Dialog", "Connection Status"))
        self.progressBar.setValue(0)


class NyvoNetHunterApp(QDialog):
    api_key = "mWNfs+SWsyZk+Wx6r5AyGw==cFD5QGOQyTJo3Xzb"

    def make_api_call(self, ip: str) -> str:
        api_url = QtCore.QUrl(f"https://api.api-ninjas.com/v1/iplookup?address={ip}")
        api_key_sign = QByteArray("X-Api-Key".encode())
        api_key_value = QByteArray(NyvoNetHunterApp.api_key.encode())

        if not isinstance(ip, str):
            raise ValueError(
                "Invalid argument type passed for the parameter ip | Expected: (str) |"
            )

        ip = f"ip={ip}"
        ip = QByteArray(ip.encode())
        request_details = QNetworkRequest(api_url)
        request_details.setRawHeader(api_key_sign, api_key_value)

        self.network_sender = QNetworkAccessManager()

        response = self.network_sender.get(request_details)
        response.downloadProgress.connect(self.fill_progressbar_animation)

        api_event_loop = QEventLoop()
        self.empty_progressbar_animation()
        response.finished.connect(api_event_loop.quit)
        api_event_loop.exec_()

        try:
            response_dictionary = json.loads(str(response.readAll(), encoding="utf-8"))

            ip_country = response_dictionary["country"]
            ip_region = response_dictionary["region"]
            ip_city = response_dictionary["city"]
            ip_zip_code = response_dictionary["zip"]
            ip_time_zone = response_dictionary["timezone"]

            return f"IP LOCATION DETECTED:\n\nCountry: {ip_country}\nRegion: {ip_region}\nCity: {ip_city}\nZip code: {ip_zip_code}\nTimezone: {ip_time_zone}"

        except:
            return "INVALID IP."

    def set_progressbar_value(self, amount: int):
        if amount > 100:
            raise TypeError(f"The progress bar fill amount cannot be more than 100.")

        if not isinstance(amount, (int, float)):
            parameter_type = type(amount).__name__
            raise TypeError(
                f"Expected argument type for the parameter (amount): str | Not {parameter_type}"
            )

        self.ui.progressBar.setValue(amount)

    def set_lineedit_result(self):
        self.ui.label_2.clear()
        self.ui.label_2.setText(self.make_api_call(self.ui.lineEdit.text()))
        self.ui.lineEdit.clear()

    def fill_progressbar_animation(self) -> None:
        for number in range(1, 101):
            QTest.qWait(15)
            self.set_progressbar_value(number)

    def empty_progressbar_animation(self) -> None:
        for number in range(100, 1):
            self.set_progressbar_value(number)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.set_lineedit_result)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_window = NyvoNetHunterApp()

    app_window.show()
    sys.exit(app_window.exec_())
