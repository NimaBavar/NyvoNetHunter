"""
# The package and/or library imports required for the project
---
"""


from os import system as cmd_input


def _install_dependencies() -> None:
    """
    This function is is used for contributors and programmers only.
    """

    
    import sys

    installed_pacakges = sys.modules.keys()
    dependencies= ["PyQt5", "requests", "pyperclip", "folium", "socket", "tldextract"]

    required_packages = [pacakge for pacakge in dependencies if not pacakge in installed_pacakges]
    for package in required_packages:
        cmd_input(f"pip install {package}")


try:
    from PyQt5.QtNetwork import QNetworkRequest, QNetworkAccessManager, QNetworkReply
    from exceptions.direct_run_error import DirectRunError
    from abc import ABC, abstractmethod, abstractproperty
    from PyQt5.QtWidgets import QApplication, QDialog
    from requests.exceptions import ConnectionError
    from tldextract import extract as extract_url
    from PyQt5.QtCore import QPropertyAnimation
    from requests.exceptions import SSLError
    from PyQt5.QtWidgets import QSizePolicy
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
    import os
    import io

except Exception as e:
    cmd_input("echo installing python dependencies...")
    _install_dependencies()


module_is_runned_directly = __name__ == "__main__"
if module_is_runned_directly:
    raise PermissionError(
        "Database modules are not intended to run directly. They are produced for import usage only."
    )
