"""
# The package and/or library imports required for the project
---
"""

from PyQt5.QtNetwork import QNetworkRequest, QNetworkAccessManager, QNetworkReply
from exceptions.direct_run_error import DirectRunError
from abc import ABC, abstractmethod, abstractproperty
from PyQt5.QtWidgets import QApplication, QDialog
from requests.exceptions import ConnectionError
from tldextract import extract as extract_url
from PyQt5.QtCore import QPropertyAnimation
from requests.exceptions import SSLError
from PyQt5.QtCore import QEventLoop
from PyQt5.QtCore import QByteArray
from PyQt5.QtCore import pyqtSignal
from os import system as cmd_input
from ipaddress import ip_address
from PyQt5.QtCore import QThread
from PyQt5.QtCore import QObject
from PyQt5 import QtCore, QtGui
from PyQt5.QtTest import QTest
from PyQt5 import QtWidgets
from typing import Literal
from json import loads
import requests
import socket
import sys
import os

module_is_runned_directly = __name__ == "__main__"

if module_is_runned_directly:
    raise PermissionError(
        "Database modules are not intended to run directly. They are produced for import usage only."
    )
