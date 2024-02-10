"""
# The package and/or library imports required for the project
---
"""


from os import system as cmd_input


try:
    from PyQt5.QtNetwork import QNetworkRequest, QNetworkAccessManager, QNetworkReply
    from exceptions.direct_run_error import DirectRunError
    from PyQt5.QtWidgets import QApplication, QDialog
    from requests.exceptions import ConnectionError
    from tldextract import extract as extract_url
    from PyQt5.QtCore import QPropertyAnimation
    from requests.exceptions import SSLError
    from PyQt5.QtWidgets import QSizePolicy
    from libnmap.process import NmapProcess
    from libnmap.objects import NmapReport
    from libnmap.parser import NmapParser
    from abc import ABC, abstractmethod
    from PyQt5 import QtWebEngineWidgets
    from PyQt5.QtCore import QEventLoop
    from PyQt5.QtCore import QByteArray
    from PyQt5.QtCore import pyqtSignal
    from dataclasses import dataclass
    from ipaddress import ip_address
    from PyQt5.QtCore import QThread
    from PyQt5.QtCore import QObject
    from PyQt5.QtGui import QPainter
    from typing import Literal, Dict
    from PyQt5 import QtCore, QtGui
    from PyQt5.QtTest import QTest
    from PyQt5.QtGui import QIcon
    from platform import platform
    from PyQt5 import QtWidgets
    from pyperclip import copy
    from pathlib import Path
    from json import loads
    from time import sleep
    import requests
    import inspect
    import folium
    import socket
    import json
    import sys
    import io
    import os
    import re

except ModuleNotFoundError as e:
    raise ModuleNotFoundError(
            "Missing dependencies, install from the requirements file. | pip install -r main_program/requirements.txt -> In the project root directory."
    ) from e


module_is_runned_directly = __name__ == "__main__"
if module_is_runned_directly:
    raise PermissionError(
        "Database modules are not intended to run directly. They are produced for import usage only."
    )
