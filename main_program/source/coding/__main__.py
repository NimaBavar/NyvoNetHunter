#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# NyvoNetHunter main module.
BY: NyvoStudio, KhodeNima ( Nima Bavar )
---
# This project and all of its components are licensed under the AGPL-3.0 ( GNU Affero Public License v3.0 ) license agreements.
"""


from database.ui_window_dialog import Ui_Dialog
from database.packages import *


class NyvoNetHunterApp(QDialog):
    api_key = "mWNfs+SWsyZk+Wx6r5AyGw==cFD5QGOQyTJo3Xzb"

    def make_api_call(self, ip: str) -> str:
        api_url = QtCore.QUrl(f"https://api.api-ninjas.com/v1/iplookup?address={ip}")
        api_key_sign = QByteArray("X-Api-Key".encode())
        api_key_value = QByteArray(NyvoNetHunterApp.api_key.encode())

        if not isinstance(ip, str):
            raise ValueError(
                "Invalid argument type passed for the parameter ( ip ) | Expected: (str) |"
            )

        raise NotImplementedError()

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
