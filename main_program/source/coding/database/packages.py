"""
# The package and/or library imports required for the project
---
"""


from os import system as cmd_input


try:
    from dataclasses import dataclass
    from ipaddress import ip_address
    from typing import Literal, Dict
    from abc import ABC, abstractmethod
    from platform import platform
    import json
    import sys
    import io
    import os
    from pathlib import Path
    from json import loads
    from time import sleep
    import inspect
    import re
    from PyQt5.QtNetwork import QNetworkRequest, QNetworkAccessManager, QNetworkReply
    from PyQt5.QtWidgets import QApplication, QDialog
    from requests.exceptions import ConnectionError
    from PyQt5.QtCore import QPropertyAnimation
    from requests.exceptions import SSLError
    from PyQt5.QtWidgets import QSizePolicy
    from libnmap.process import NmapProcess
    from libnmap.objects import NmapReport
    from libnmap.parser import NmapParser
    from PyQt5 import QtWebEngineWidgets
    from PyQt5.QtCore import QEventLoop
    from PyQt5.QtCore import QByteArray
    from PyQt5.QtCore import pyqtSignal
    from PyQt5.QtCore import QThread
    from PyQt5.QtCore import QObject
    from PyQt5.QtGui import QPainter
    from PyQt5 import QtCore, QtGui
    from PyQt5.QtTest import QTest
    from PyQt5.QtGui import QIcon
    from PyQt5 import QtWidgets
    from pyperclip import copy
    from tldextract import extract as extract_url
    import socket
    import folium
    import requests
    from exceptions.direct_run_error import DirectRunError

except ModuleNotFoundError as e:
    raise ModuleNotFoundError(
            "Missing dependencies, install from the requirements file. | pip install -r main_program/requirements.txt -> In the project root directory."
    ) from e


module_is_runned_directly = __name__ == "__main__"
if module_is_runned_directly:
    raise PermissionError(
        "Database modules are not intended to run directly. They are produced for import usage only."
    )
