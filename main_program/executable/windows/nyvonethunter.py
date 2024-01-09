#!/usr/bin/env python3
"""
# The main launcher for Windows operating systems.
"""


def setup_database_import_path() -> None:
    from sys import path as module_paths
    import pathlib

    project_root_directory = pathlib.Path.cwd()

    module_paths.append(f"{project_root_directory}/main_program/source/ui_design/resources")

setup_database_import_path()


try:
    from PyQt5.QtNetwork import QNetworkRequest, QNetworkAccessManager, QNetworkReply
    from abc import ABC, abstractmethod, abstractproperty
    from PyQt5.QtWidgets import QApplication, QDialog
    from requests.exceptions import ConnectionError
    from PyQt5.QtCore import QTemporaryDir, QFile
    from tldextract import extract as extract_url
    from PyQt5.QtCore import QPropertyAnimation
    from requests.exceptions import SSLError
    from PyQt5.QtWidgets import QSizePolicy
    from PyQt5.QtCore import QTemporaryDir
    from PyQt5 import QtWebEngineWidgets
    from PyQt5.QtCore import QEventLoop
    from PyQt5.QtCore import QByteArray
    from PyQt5.QtCore import pyqtSignal
    from os import system as cmd_input
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
    from pathlib import Path
    import resource_storage
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
    raise ModuleNotFoundError(
        "Please activate the project main virtual environment in order to access direct execute permission."
    ) from e


def setup_temp_directory() -> QTemporaryDir:
    home_path = os.environ["HOME"]

    temporary_directory = QTemporaryDir(f"{home_path}/nyvonethunter_temp")
    temporary_directory.setAutoRemove(False)

    file_manager = QFile("temp_dir_manager")


    required_resources = [":/pictures/target_icon.png", ":/html_files/base_state.html", ":/html_files/spoof_result.html"]

    file_manager.copy(":/pictures/target_icon.png", f"{temporary_directory.path()}/target_icon.png")
    file_manager.copy(":/html_files/base_state.html", f"{temporary_directory.path()}/base_state.html")
    file_manager.copy(":/html_files/spoof_result.html", f"{temporary_directory.path()}/spoof_result.html")

    cmd_input(f"chmod +rwx {temporary_directory.path()}/spoof_result.html")

    return temporary_directory


temporary_resource_file = setup_temp_directory()


class DirectRunError(Exception):
    """Improper direct run of a module"""

    def __init__(self, error_message: str):
        self.error_message = error_message

    @property
    def error_message(self) -> str:
        return self._error_message

    @error_message.setter
    def error_message(self, message) -> str:
        message_is_string = isinstance(message, str)
        message_is_not_valid = not message_is_string

        if message_is_not_valid:
            error_message_argument_type = type(message).__name__
            raise ValueError(
                f"Expected argument type passed for the parameter ( error_message ): ( str ) | Not: ( {error_message_argument_type} )"
            )

        self._error_message = message


class UnexpectedArgumentTypeError(ValueError):
    def __init__(self, inputted_argument, expected_argument_type: object) -> None:
        self.passed_argument = inputted_argument
        self.passed_argument_type = inputted_argument
        self.expected_argument_type = expected_argument_type

        self._generate_error_message()
        super().__init__(self.error_message)

    def _generate_error_message(self):
        self.error_message = (
            f"Expected argument type passed for the parameter \
( {self.passed_argument} ): ( {self.expected_argument_type} ) | Not ( {self.passed_argument_type} )."
            )
        
    @property
    def passed_argument_type(self):
        return self._passed_argument_type
    
    @passed_argument_type.setter
    def passed_argument_type(self, argument_type):
        self._passed_argument_type = type(argument_type).__name__

    @property
    def expected_argument_type(self):
        return self._expected_argument_type
    
    @expected_argument_type.setter
    def expected_argument_type(self, argument):
        if not inspect.isclass(argument):
            raise ValueError("The ( expected_argument_type ) argument must be object| e.x: ( str, tuple... )")
        
        self._expected_argument_type = argument.__name__


class MapSpoofer(QObject):
    location_spoofed = pyqtSignal()
    saved_as_html = pyqtSignal()

    def __init__(self, latitude: int, longitude: int):
        self.latitude = latitude
        self.longitude = longitude

        self.generated = False

        super(QObject, self).__init__()

    def start(self):
        self.generated = True

        self._map_image_html = folium.Map(
        location=[self.latitude, self.longitude], 
        tiles="Cartodb dark_matter",
        max_bounds=True,
        zoom_start=2, 
        max_zoom=13,
        min_zoom=2, 
        )

        target_icon = folium.CustomIcon(
            icon_image=f"{temporary_resource_file.path()}/target_icon.png",
            icon_size=[65, 65]
        )
        
        target_marker = folium.Marker(
            location=[self.latitude, self.longitude],
            tooltip="Exact target location.",
            icon=target_icon
        )

        target_radius_marker = folium.CircleMarker(
            location=[self.latitude, self.longitude],
            tooltip="Target is in this area.",
            radius=44,
            color="red",
            fill_color='red',
        )


        target_marker.add_to(self._map_image_html)
        target_radius_marker.add_to(self._map_image_html)

        self.location_spoofed.emit()
        return self._map_image_html

    def save_as_html_file(self, file_path: str) -> None:
        self.saved_as_html.emit()
        self._map_image_html.save(outfile=file_path)

    def save_as_geojson(self, file_path: str) -> None:
        if not self.generated:
            raise PermissionError("No spoof result to save, please finish the spoofing operation before attempting to save.")

        if not isinstance(file_path, str):
            raise UnexpectedArgumentTypeError(inputted_argument=file_path, expected_argument_type=str)
        
        map_image_geojson = json.loads(self._map_image_html.to_json())

        with open(file_path, "w") as geojson_file:
            json.dump(map_image_geojson, geojson_file, indent=4)

    def save_as_bytes(self):
        if not self.generated:
            raise PermissionError("No spoof result to save, please finish the spoofing operation before attempting to save.")

        byte_data = io.BytesIO()
        self._map_image_html.save(byte_data, close_file=False)
        self.map_image_bytes = byte_data

        return self.map_image_bytes
    
    def set_latitude(self, latitude) -> None:
        self.latitude = latitude

    def set_longitude(self, longitude) -> None:
        self.longitude = longitude


class Connectable(ABC):
    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    @abstractproperty
    def endpoint(self) -> str:
        return self._endpoint

    @endpoint.setter
    def endpoint(self, _endpoint):
        if not isinstance(_endpoint, str):
            endpoint_argument_type = type(_endpoint).__name__
            raise ValueError(
                f"Expected argument type passed for the parameter ( endpoint ): ( str ) | Not {endpoint_argument_type}"
            )

        self._endpoint = _endpoint
        

class NyvoNetHunterRequestManager(QObject):
    request_started = pyqtSignal()
    request_sent = pyqtSignal()

    failed_to_send = pyqtSignal()

    received_valid_response = pyqtSignal()
    received_invalid_response = pyqtSignal()


    def __init__(
        self,
        url: str,
        data: Dict,
        headers: Dict,
        method: Literal["get", "post", "put", "delete"],
    ):
        self.url = url
        self.data = data
        self.headers = headers
        self.method = method

        super(QObject, self).__init__()

    def fire(self) -> str:
        self.request_started.emit()

        try:
            self.response = requests.request(method=self.method, url=self.url, data=self.data, headers=self.headers, timeout=20)
            self.request_sent.emit()

        except Exception as e:
            self.failed_to_send.emit()
            return

        if self.response.ok:
            self.received_valid_response.emit()

            return self.response

        self.received_invalid_response.emit()
        return self.response

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, _url):
        if not isinstance(_url, str):
            url_argument_type = type(_url).__name__
            raise ValueError(
                f"Expected argument type passed for the parameter( url ): ( str ) | Not ( {url_argument_type}"
            )

        url_is_invalid = not is_valid_url(_url)
        if url_is_invalid:
            raise TypeError("That is not a valid url.")

        self._url = _url

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, _data):
        if not isinstance(_data, dict):
            data_argument_type = type(_data).__name__
            raise ValueError(
                f"Expected argument type passed for the parameter ( data ): ( dict ) | Not: ( {data_argument_type} )"
            )

        self._data = _data

    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, _headers):
        if not isinstance(_headers, dict):
            headers_argument_type = type(_headers).__name__
            raise ValueError(
                f"Expected argument type passed for the parameter ( headers ): ( dict ) | Not: ( {headers_argument_type} )"
            )

        self._headers = _headers

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, _method):
        available_http_methods = ["get", "post", "put", "delete"]

        if not isinstance(_method, str):
            method_argument_type = type(_method).__name__
            raise ValueError(
                f"Expected argument types passed for the parameter ( method ): ( str ) | Not: {method_argument_type}"
            )

        if not _method in available_http_methods:
            raise TypeError("That is not a valid http method.")

        self._method = _method


class NyvoNetHunterIpAddress(Connectable):
    def __init__(self, ip_address: str):
        self.endpoint = ip_address

    @property
    def endpoint(self) -> str:
        return self._ip_address

    @endpoint.setter
    def endpoint(self, _ip_address):
        if not isinstance(_ip_address, str):
            endpoint_argument_type = type(_ip_address).__name__
            raise ValueError(
                f"Expected argument type passed for the parameter ( endpoint ): ( str ) | Not: {endpoint_argument_type}"
            )

        if not is_valid_ip(_ip_address):
            raise TypeError("Invalid Ip address passed.")

        self._ip_address = _ip_address


class NyvoNetHunterUrl(Connectable):
    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    @property
    def endpoint(self) -> str:
        return self._endpoint

    @endpoint.setter
    def endpoint(self, _endpoint) -> str:
        if not isinstance(_endpoint, str):
            endpoint_argument_type = type(_endpoint).__name__
            raise ValueError(
                f"Expected argument type passed for the parameter ( endpoint ): ( str ) | Not: {endpoint_argument_type}"
            )

        if not is_valid_url(_endpoint):
            raise TypeError("Invalid url passed.")
        
        self._endpoint = _endpoint


def generate_valid_connectable(endpoint: str) -> Connectable:
    if not isinstance(endpoint, str):
        endpoint_argument_type = type(endpoint).__name__
        raise ValueError(
            f"Expected argument type passed for the parameter ( endpoint ): str | Not: {endpoint_argument_type}"
        )

    endpoint_type = find_endpoint_type(endpoint)

    try:
        if endpoint_type == "ip":
            generated_connectable = NyvoNetHunterIpAddress(endpoint)

        if endpoint_type == "url":
            generated_connectable = NyvoNetHunterUrl(endpoint)

    except ValueError:
        raise ValueError("Invalid ip or URL.")

    return generated_connectable


def find_endpoint_type(connectable: [Connectable, str]) -> Literal["ip", "url"]:
    """
    Returns:
        str: ( `ip` ), ( `url` )
    """

    if not isinstance(connectable, (Connectable, str)):
        connectable_argument_type = type(connectable).__name__
        raise ValueError(
            f"Expected argument types passed for the parameter ( connectable, str ): Connectable | Not: ( {connectable_argument_type} )"
        )

    if isinstance(connectable, str):
        connectable_endpoint = connectable

    else:
        connectable_endpoint = connectable.endpoint

    endpoint_is_ip_address = is_valid_ip(connectable_endpoint)
    endpoint_is_url = is_valid_url(connectable_endpoint)

    if not endpoint_is_ip_address and not endpoint_is_url:
        raise TypeError("Invalid IP or URL.")

    if endpoint_is_ip_address:
        return "ip"

    if endpoint_is_url:
        return "url"


def is_valid_ip(ip: str) -> bool:
    if not isinstance(ip, str):
        ip_argument_type = type(ip).__name__
        raise ValueError(
            f"Expected argument type passed for the parameter ( ip ): ( str ) | Not: ( {ip_argument_type} )"
        )

    try:
        ip_address(ip)
        return True

    except ValueError:
        return False


def is_valid_ipv4(ip: str) -> bool:
    if not isinstance(ip, str):
        ip_argument_type = type(ip).__name__
        raise ValueError(
            f"Expected argument type passed for the parameter ( ip ): ( str ) | Not: ( {ip_argument_type} )"
        )

    if not is_valid_ip(ip):
        return False

    ip_version = ip_address(ip).version
    ip_version_is_ipv4 = ip_version == 4

    if ip_version_is_ipv4:
        return True

    return False


def is_valid_ipv6(ip: str):
    if not isinstance(ip, str):
        ip_argument_type = type(ip).__name__
        raise ValueError(
            f"Expected argument type passed for the parameter ( ip ): ( str ) | Not: ( {ip_argument_type} )"
        )

    if not is_valid_ip(ip):
        return False

    ip_version = ip_address(ip).version
    ip_version_is_ipv6 = ip_version == 6

    if ip_version_is_ipv6:
        return True

    return False


def is_valid_url(url: str) -> bool:
    if not isinstance(url, str):
        url_argument_type = type(url).__name__
        raise ValueError(
            f"Expected argument type passed for the parameter ( url ): (str) | Not: ( {url_argument_type} )"
        )

    url_contains_schema = url.startswith("https://") or url.startswith("http://")

    if not url_contains_schema:
        url = f"http://{url}"

    extracted_url_segments = (extract_url(url))._asdict()
    extracted_segments_list = [segment for segment in extracted_url_segments.values()]

    url_has_domain_name = bool(extracted_segments_list[1])
    url_has_top_level_domain = bool(extracted_segments_list[2])

    url_is_valid = all([url_has_domain_name, url_has_top_level_domain])

    if url_is_valid:
        return True

    return False


def clean_terminal() -> None:
    runner_operating_system = platform(terse=True)
    operating_system_is_windows = runner_operating_system.lower().startswith("windows")
    operating_system_is_linux = runner_operating_system.lower().startswith("linux")

    if operating_system_is_windows:
        cmd_input("cls")
        return

    if operating_system_is_linux:
        cmd_input("clear")


def simplify_long_string(text: str) -> str:
    """Simplifies a long text for previews.

    ex: MyNameIsAlex -> MyName...
    """

    if not isinstance(text, str):
        raise UnexpectedArgumentTypeError(text, str)


    text_lenght = len(text)
    if not text_lenght >= 6:
        return text
    
    simplified_string = f"{text[0:5]}..."
    return simplified_string


class ConnectionStatusChecker(QObject):
    spotted_connection = pyqtSignal()
    lost_connection = pyqtSignal()

    def run(self):
        """
        Host: 8.8.8.8 (google-public-dns-a.google.com)
        OpenPort: 53/tcp
        Service: domain (DNS/TCP)
        """

        timeout = 3
        host = "8.8.8.8"
        port = 53
        connection_is_available = None

        self.lost_connection.emit()

        while True:
            try:
                socket.setdefaulttimeout(timeout)
                socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))

                if connection_is_available == True:
                    continue

                self.spotted_connection.emit()
                connection_is_available = True

            except socket.error:
                if connection_is_available == False:
                    continue

                self.lost_connection.emit()
                connection_is_available = False


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1192, 685)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        Dialog.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pictures/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setWindowOpacity(5.0)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(430, 530, 211, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setWhatsThis("")
        self.pushButton.setStyleSheet("QPushButton{ border: 2px solid red; background-color: orange }\n"
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
"        font: bold large \"Arial\";\n"
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
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pictures/pushbuttonicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(35, 35))
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(250, 490, 561, 31))
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
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhSensitiveData)
        self.lineEdit.setMaxLength(50)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(250, 180, 561, 301))
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
        self.callstatusLabel = QtWidgets.QLabel(Dialog)
        self.callstatusLabel.setGeometry(QtCore.QRect(480, 100, 121, 31))
        self.callstatusLabel.setStyleSheet("QLabel{ border: 2px solid red; background-color: orange }\n"
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
"        font: bold large \"Arial\";\n"
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
"}")
        self.callstatusLabel.setObjectName("callstatusLabel")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(250, 140, 561, 31))
        self.progressBar.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.progressBar.setStyleSheet("QProgressBar {\n"
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
"        font: bold large \"Arial\";\n"
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
"")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.responseLabel = QtWidgets.QLabel(Dialog)
        self.responseLabel.setGeometry(QtCore.QRect(280, 190, 501, 281))
        self.responseLabel.setText("")
        self.responseLabel.setObjectName("responseLabel")
        self.graphicsView_2 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_2.setGeometry(QtCore.QRect(50, 180, 191, 301))
        self.graphicsView_2.setStyleSheet("QGraphicsView { border: 2px solid red; background-color: orange }\n"
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
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.countryCheckBox = QtWidgets.QCheckBox(Dialog)
        self.countryCheckBox.setGeometry(QtCore.QRect(60, 200, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.countryCheckBox.setFont(font)
        self.countryCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.countryCheckBox.setStyleSheet("QCheckBox {\n"
"  width: 35px;\n"
"  height: 35px;\n"
"  cursor: pointer;\n"
"  margin-right: -22px;\n"
"  appearance: none;\n"
"  border-radius: 5px;\n"
"  background-color: #6593cf;\n"
"   : 2;\n"
"   : all 0.3s;\n"
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
"   : all 0.3s;\n"
"}\n"
"\n"
"QCheckBox::before {\n"
"  content: \"\";\n"
"  background-color: #6593cf;\n"
"  position: relative;\n"
"  display: flex;\n"
"  top: 45%;\n"
"  left: 50%;\n"
"  width: 55px;\n"
"  height: 3px;\n"
"  border-radius: 25px;\n"
"  : translate(100px, 0px) scale(0);\n"
"   : ease-out 0.15s;\n"
"}\n"
"\n"
"QCheckBox:checked::before {\n"
"  : translateX(2em);\n"
"  top: 12px;\n"
"   : ease-out 0.15s;\n"
"}\n"
"\n"
"QcheckBox:hover {\n"
"  : translate(4px, 4px);\n"
"   : ease-out 0.15s;\n"
"  background-color: #6593cf;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"  : translate(4px, 4px);\n"
"   : ease-out 0.15s;\n"
"  background-color: #6593cf;\n"
"}\n"
"\n"
".svg-icon {\n"
"  position: absolute;\n"
"  width: 25px;\n"
"  height: 25px;\n"
"  display: flex;\n"
"   : 3;\n"
"  top: 35%;\n"
"  left: 11%;\n"
"  color: #fefefe;\n"
"  font-family: \"Gill Sans\", \"Gill Sans MT\", Calibri, \"Trebuchet MS\", sans-serif;\n"
"  : rotate(0deg) scale(0);\n"
"   : ease-in 0.2s;\n"
"}\n"
"\n"
"QCheckBoxchecked ~ .svg-icon {\n"
"  : rotate(360deg) scale(1);\n"
"   : ease-in 0.2s;\n"
"}\n"
"")
        self.countryCheckBox.setObjectName("countryCheckBox")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 140, 191, 31))
        self.label_3.setStyleSheet("QLabel{ border: 2px solid red; background-color: orange }\n"
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
"        font: bold large \"Arial\";\n"
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
"}")
        self.label_3.setObjectName("label_3")
        self.regionCheckBox = QtWidgets.QCheckBox(Dialog)
        self.regionCheckBox.setGeometry(QtCore.QRect(60, 220, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.regionCheckBox.setFont(font)
        self.regionCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.regionCheckBox.setStyleSheet("QCheckBox {\n"
"  width: 35px;\n"
"  height: 35px;\n"
"  cursor: pointer;\n"
"  margin-right: -22px;\n"
"  appearance: none;\n"
"  border-radius: 5px;\n"
"  background-color: #6593cf;\n"
"   : 2;\n"
"   : all 0.3s;\n"
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
"   : all 0.3s;\n"
"}\n"
"\n"
"QCheckBox::before {\n"
"  content: \"\";\n"
"  background-color: #6593cf;\n"
"  position: relative;\n"
"  display: flex;\n"
"  top: 45%;\n"
"  left: 50%;\n"
"  width: 55px;\n"
"  height: 3px;\n"
"  border-radius: 25px;\n"
"  : translate(100px, 0px) scale(0);\n"
"   : ease-out 0.15s;\n"
"}\n"
"\n"
"QCheckBox:checked::before {\n"
"  : translateX(2em);\n"
"  top: 12px;\n"
"   : ease-out 0.15s;\n"
"}\n"
"\n"
"QcheckBox:hover {\n"
"  : translate(4px, 4px);\n"
"   : ease-out 0.15s;\n"
"  background-color: #6593cf;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"  : translate(4px, 4px);\n"
"   : ease-out 0.15s;\n"
"  background-color: #6593cf;\n"
"}\n"
"\n"
".svg-icon {\n"
"  position: absolute;\n"
"  width: 25px;\n"
"  height: 25px;\n"
"  display: flex;\n"
"   : 3;\n"
"  top: 35%;\n"
"  left: 11%;\n"
"  color: #fefefe;\n"
"  font-family: \"Gill Sans\", \"Gill Sans MT\", Calibri, \"Trebuchet MS\", sans-serif;\n"
"  : rotate(0deg) scale(0);\n"
"   : ease-in 0.2s;\n"
"}\n"
"\n"
"QCheckBoxchecked ~ .svg-icon {\n"
"  : rotate(360deg) scale(1);\n"
"   : ease-in 0.2s;\n"
"}\n"
"")
        self.regionCheckBox.setObjectName("regionCheckBox")
        self.cityCheckBox = QtWidgets.QCheckBox(Dialog)
        self.cityCheckBox.setGeometry(QtCore.QRect(60, 240, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cityCheckBox.setFont(font)
        self.cityCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cityCheckBox.setStyleSheet("QCheckBox {\n"
"  width: 35px;\n"
"  height: 35px;\n"
"  cursor: pointer;\n"
"  margin-right: -22px;\n"
"  appearance: none;\n"
"  border-radius: 5px;\n"
"  background-color: #6593cf;\n"
"   : 2;\n"
"   : all 0.3s;\n"
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
"   : all 0.3s;\n"
"}\n"
"\n"
"QCheckBox::before {\n"
"  content: \"\";\n"
"  background-color: #6593cf;\n"
"  position: relative;\n"
"  display: flex;\n"
"  top: 45%;\n"
"  left: 50%;\n"
"  width: 55px;\n"
"  height: 3px;\n"
"  border-radius: 25px;\n"
"  : translate(100px, 0px) scale(0);\n"
"   : ease-out 0.15s;\n"
"}\n"
"\n"
"QCheckBox:checked::before {\n"
"  : translateX(2em);\n"
"  top: 12px;\n"
"   : ease-out 0.15s;\n"
"}\n"
"\n"
"QcheckBox:hover {\n"
"  : translate(4px, 4px);\n"
"   : ease-out 0.15s;\n"
"  background-color: #6593cf;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"  : translate(4px, 4px);\n"
"   : ease-out 0.15s;\n"
"  background-color: #6593cf;\n"
"}\n"
"\n"
".svg-icon {\n"
"  position: absolute;\n"
"  width: 25px;\n"
"  height: 25px;\n"
"  display: flex;\n"
"   : 3;\n"
"  top: 35%;\n"
"  left: 11%;\n"
"  color: #fefefe;\n"
"  font-family: \"Gill Sans\", \"Gill Sans MT\", Calibri, \"Trebuchet MS\", sans-serif;\n"
"  : rotate(0deg) scale(0);\n"
"   : ease-in 0.2s;\n"
"}\n"
"\n"
"QCheckBoxchecked ~ .svg-icon {\n"
"  : rotate(360deg) scale(1);\n"
"   : ease-in 0.2s;\n"
"}\n"
"")
        self.cityCheckBox.setObjectName("cityCheckBox")
        self.zipcodeCheckBox = QtWidgets.QCheckBox(Dialog)
        self.zipcodeCheckBox.setGeometry(QtCore.QRect(60, 260, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.zipcodeCheckBox.setFont(font)
        self.zipcodeCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.zipcodeCheckBox.setStyleSheet("QCheckBox {\n"
"  width: 35px;\n"
"  height: 35px;\n"
"  cursor: pointer;\n"
"  margin-right: -22px;\n"
"  appearance: none;\n"
"  border-radius: 5px;\n"
"  background-color: #6593cf;\n"
"   : 2;\n"
"   : all 0.3s;\n"
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
"   : all 0.3s;\n"
"}\n"
"\n"
"QCheckBox::before {\n"
"  content: \"\";\n"
"  background-color: #6593cf;\n"
"  position: relative;\n"
"  display: flex;\n"
"  top: 45%;\n"
"  left: 50%;\n"
"  width: 55px;\n"
"  height: 3px;\n"
"  border-radius: 25px;\n"
"  : translate(100px, 0px) scale(0);\n"
"   : ease-out 0.15s;\n"
"}\n"
"\n"
"QCheckBox:checked::before {\n"
"  : translateX(2em);\n"
"  top: 12px;\n"
"   : ease-out 0.15s;\n"
"}\n"
"\n"
"QcheckBox:hover {\n"
"  : translate(4px, 4px);\n"
"   : ease-out 0.15s;\n"
"  background-color: #6593cf;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"  : translate(4px, 4px);\n"
"   : ease-out 0.15s;\n"
"  background-color: #6593cf;\n"
"}\n"
"\n"
".svg-icon {\n"
"  position: absolute;\n"
"  width: 25px;\n"
"  height: 25px;\n"
"  display: flex;\n"
"   : 3;\n"
"  top: 35%;\n"
"  left: 11%;\n"
"  color: #fefefe;\n"
"  font-family: \"Gill Sans\", \"Gill Sans MT\", Calibri, \"Trebuchet MS\", sans-serif;\n"
"  : rotate(0deg) scale(0);\n"
"   : ease-in 0.2s;\n"
"}\n"
"\n"
"QCheckBoxchecked ~ .svg-icon {\n"
"  : rotate(360deg) scale(1);\n"
"   : ease-in 0.2s;\n"
"}\n"
"")
        self.zipcodeCheckBox.setObjectName("zipcodeCheckBox")
        self.timezoneCheckBox = QtWidgets.QCheckBox(Dialog)
        self.timezoneCheckBox.setGeometry(QtCore.QRect(60, 280, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.timezoneCheckBox.setFont(font)
        self.timezoneCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.timezoneCheckBox.setStyleSheet("QCheckBox {\n"
"  width: 35px;\n"
"  height: 35px;\n"
"  cursor: pointer;\n"
"  margin-right: -22px;\n"
"  appearance: none;\n"
"  border-radius: 5px;\n"
"  background-color: #6593cf;\n"
"   : 2;\n"
"   : all 0.3s;\n"
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
"   : all 0.3s;\n"
"}\n"
"\n"
"QCheckBox::before {\n"
"  content: \"\";\n"
"  background-color: #6593cf;\n"
"  position: relative;\n"
"  display: flex;\n"
"  top: 45%;\n"
"  left: 50%;\n"
"  width: 55px;\n"
"  height: 3px;\n"
"  border-radius: 25px;\n"
"  : translate(100px, 0px) scale(0);\n"
"   : ease-out 0.15s;\n"
"}\n"
"\n"
"QCheckBox:checked::before {\n"
"  : translateX(2em);\n"
"  top: 12px;\n"
"   : ease-out 0.15s;\n"
"}\n"
"\n"
"QcheckBox:hover {\n"
"  : translate(4px, 4px);\n"
"   : ease-out 0.15s;\n"
"  background-color: #6593cf;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"  : translate(4px, 4px);\n"
"   : ease-out 0.15s;\n"
"  background-color: #6593cf;\n"
"}\n"
"\n"
".svg-icon {\n"
"  position: absolute;\n"
"  width: 25px;\n"
"  height: 25px;\n"
"  display: flex;\n"
"   : 3;\n"
"  top: 35%;\n"
"  left: 11%;\n"
"  color: #fefefe;\n"
"  font-family: \"Gill Sans\", \"Gill Sans MT\", Calibri, \"Trebuchet MS\", sans-serif;\n"
"  : rotate(0deg) scale(0);\n"
"   : ease-in 0.2s;\n"
"}\n"
"\n"
"QCheckBoxchecked ~ .svg-icon {\n"
"  : rotate(360deg) scale(1);\n"
"   : ease-in 0.2s;\n"
"}\n"
"")
        self.timezoneCheckBox.setObjectName("timezoneCheckBox")
        self.ispCheckBox = QtWidgets.QCheckBox(Dialog)
        self.ispCheckBox.setGeometry(QtCore.QRect(60, 300, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ispCheckBox.setFont(font)
        self.ispCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ispCheckBox.setStyleSheet("QCheckBox {\n"
"  width: 35px;\n"
"  height: 35px;\n"
"  cursor: pointer;\n"
"  margin-right: -22px;\n"
"  appearance: none;\n"
"  border-radius: 5px;\n"
"  background-color: #6593cf;\n"
"   : 2;\n"
"   : all 0.3s;\n"
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
"   : all 0.3s;\n"
"}\n"
"\n"
"QCheckBox::before {\n"
"  content: \"\";\n"
"  background-color: #6593cf;\n"
"  position: relative;\n"
"  display: flex;\n"
"  top: 45%;\n"
"  left: 50%;\n"
"  width: 55px;\n"
"  height: 3px;\n"
"  border-radius: 25px;\n"
"  : translate(100px, 0px) scale(0);\n"
"   : ease-out 0.15s;\n"
"}\n"
"\n"
"QCheckBox:checked::before {\n"
"  : translateX(2em);\n"
"  top: 12px;\n"
"   : ease-out 0.15s;\n"
"}\n"
"\n"
"QcheckBox:hover {\n"
"  : translate(4px, 4px);\n"
"   : ease-out 0.15s;\n"
"  background-color: #6593cf;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"  : translate(4px, 4px);\n"
"   : ease-out 0.15s;\n"
"  background-color: #6593cf;\n"
"}\n"
"\n"
".svg-icon {\n"
"  position: absolute;\n"
"  width: 25px;\n"
"  height: 25px;\n"
"  display: flex;\n"
"   : 3;\n"
"  top: 35%;\n"
"  left: 11%;\n"
"  color: #fefefe;\n"
"  font-family: \"Gill Sans\", \"Gill Sans MT\", Calibri, \"Trebuchet MS\", sans-serif;\n"
"  : rotate(0deg) scale(0);\n"
"   : ease-in 0.2s;\n"
"}\n"
"\n"
"QCheckBoxchecked ~ .svg-icon {\n"
"  : rotate(360deg) scale(1);\n"
"   : ease-in 0.2s;\n"
"}\n"
"")
        self.ispCheckBox.setObjectName("ispCheckBox")
        self.latitudeCheckBox = QtWidgets.QCheckBox(Dialog)
        self.latitudeCheckBox.setGeometry(QtCore.QRect(60, 330, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.latitudeCheckBox.setFont(font)
        self.latitudeCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.latitudeCheckBox.setStyleSheet("QCheckBox {\n"
"  width: 35px;\n"
"  height: 35px;\n"
"  cursor: pointer;\n"
"  margin-right: -22px;\n"
"  appearance: none;\n"
"  border-radius: 5px;\n"
"  background-color: #6593cf;\n"
"   : 2;\n"
"   : all 0.3s;\n"
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
"   : all 0.3s;\n"
"}\n"
"\n"
"QCheckBox::before {\n"
"  content: \"\";\n"
"  background-color: #6593cf;\n"
"  position: relative;\n"
"  display: flex;\n"
"  top: 45%;\n"
"  left: 50%;\n"
"  width: 55px;\n"
"  height: 3px;\n"
"  border-radius: 25px;\n"
"  : translate(100px, 0px) scale(0);\n"
"   : ease-out 0.15s;\n"
"}\n"
"\n"
"QCheckBox:checked::before {\n"
"  : translateX(2em);\n"
"  top: 12px;\n"
"   : ease-out 0.15s;\n"
"}\n"
"\n"
"QcheckBox:hover {\n"
"  : translate(4px, 4px);\n"
"   : ease-out 0.15s;\n"
"  background-color: #6593cf;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"  : translate(4px, 4px);\n"
"   : ease-out 0.15s;\n"
"  background-color: #6593cf;\n"
"}\n"
"\n"
".svg-icon {\n"
"  position: absolute;\n"
"  width: 25px;\n"
"  height: 25px;\n"
"  display: flex;\n"
"   : 3;\n"
"  top: 35%;\n"
"  left: 11%;\n"
"  color: #fefefe;\n"
"  font-family: \"Gill Sans\", \"Gill Sans MT\", Calibri, \"Trebuchet MS\", sans-serif;\n"
"  : rotate(0deg) scale(0);\n"
"   : ease-in 0.2s;\n"
"}\n"
"\n"
"QCheckBoxchecked ~ .svg-icon {\n"
"  : rotate(360deg) scale(1);\n"
"   : ease-in 0.2s;\n"
"}\n"
"")
        self.latitudeCheckBox.setObjectName("latitudeCheckBox")
        self.longitudeCheckBox = QtWidgets.QCheckBox(Dialog)
        self.longitudeCheckBox.setGeometry(QtCore.QRect(60, 350, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.longitudeCheckBox.setFont(font)
        self.longitudeCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.longitudeCheckBox.setStyleSheet("QCheckBox {\n"
"  width: 35px;\n"
"  height: 35px;\n"
"  cursor: pointer;\n"
"  margin-right: -22px;\n"
"  appearance: none;\n"
"  border-radius: 5px;\n"
"  background-color: #6593cf;\n"
"   : 2;\n"
"   : all 0.3s;\n"
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
"   : all 0.3s;\n"
"}\n"
"\n"
"QCheckBox::before {\n"
"  content: \"\";\n"
"  background-color: #6593cf;\n"
"  position: relative;\n"
"  display: flex;\n"
"  top: 45%;\n"
"  left: 50%;\n"
"  width: 55px;\n"
"  height: 3px;\n"
"  border-radius: 25px;\n"
"  : translate(100px, 0px) scale(0);\n"
"   : ease-out 0.15s;\n"
"}\n"
"\n"
"QCheckBox:checked::before {\n"
"  : translateX(2em);\n"
"  top: 12px;\n"
"   : ease-out 0.15s;\n"
"}\n"
"\n"
"QcheckBox:hover {\n"
"  : translate(4px, 4px);\n"
"   : ease-out 0.15s;\n"
"  background-color: #6593cf;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"  : translate(4px, 4px);\n"
"   : ease-out 0.15s;\n"
"  background-color: #6593cf;\n"
"}\n"
"\n"
".svg-icon {\n"
"  position: absolute;\n"
"  width: 25px;\n"
"  height: 25px;\n"
"  display: flex;\n"
"   : 3;\n"
"  top: 35%;\n"
"  left: 11%;\n"
"  color: #fefefe;\n"
"  font-family: \"Gill Sans\", \"Gill Sans MT\", Calibri, \"Trebuchet MS\", sans-serif;\n"
"  : rotate(0deg) scale(0);\n"
"   : ease-in 0.2s;\n"
"}\n"
"\n"
"QCheckBoxchecked ~ .svg-icon {\n"
"  : rotate(360deg) scale(1);\n"
"   : ease-in 0.2s;\n"
"}\n"
"")
        self.longitudeCheckBox.setObjectName("longitudeCheckBox")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 10, 191, 31))
        self.label_4.setStyleSheet("QLabel{ border: 2px solid red; background-color: orange }\n"
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
"        font: bold large \"Arial\";\n"
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
"}")
        self.label_4.setObjectName("label_4")
        self.connection_status_label = QtWidgets.QLabel(Dialog)
        self.connection_status_label.setGeometry(QtCore.QRect(50, 50, 191, 81))
        self.connection_status_label.setText("")
        self.connection_status_label.setObjectName("connection_status_label")
        self.webView = QtWebEngineWidgets.QWebEngineView(Dialog)
        self.webView.setGeometry(QtCore.QRect(820, 180, 300, 301))

        self.no_connection_icon = QtGui.QPixmap(":/pictures/no_connection_icon.png")
        self.connected_icon = QtGui.QPixmap(":/pictures/connected_icon.png")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "NyvoNetHunter"))
        self.pushButton.setToolTip(_translate("Dialog", "<html><head/><body><p>Examine the ENDPOINT!</p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Examine"))
        self.lineEdit.setToolTip(_translate("Dialog", "<html><head/><body><p>IP example: <span style=\" font-style:italic; text-decoration: underline;\">144.145.146.147</span><span style=\" font-weight:400;\">. </span>( IP addresses maximum octet digit is 255 )</p><p>URL example: <span style=\" font-style:italic; text-decoration: underline;\">https://github.com</span> OR <span style=\" font-style:italic; text-decoration: underline;\">https://discord.com</span><span style=\" font-weight:400;\">.</span></p><p><br/></p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Enter your desired IP or URL to examine: "))
        self.graphicsView.setToolTip(_translate("Dialog", "<html><head/><body><p>The examine operation outputs will be shown <span style=\" font-style:italic; text-decoration: underline;\">here.</span></p></body></html>"))
        self.callstatusLabel.setText(_translate("Dialog", "Awaiting..."))
        self.progressBar.setToolTip(_translate("Dialog", "<html><head/><body><p>Examining...</p></body></html>"))
        self.progressBar.setFormat(_translate("Dialog", "%p%"))
        self.graphicsView_2.setToolTip(_translate("Dialog", "<html><head/><body><p>The examine operation outputs will be shown <span style=\" font-style:italic; text-decoration: underline;\">here.</span></p></body></html>"))
        self.countryCheckBox.setText(_translate("Dialog", "Country"))
        self.label_3.setText(_translate("Dialog", "     Examine options"))
        self.regionCheckBox.setText(_translate("Dialog", "Region"))
        self.cityCheckBox.setText(_translate("Dialog", "City"))
        self.zipcodeCheckBox.setText(_translate("Dialog", "Zip code"))
        self.timezoneCheckBox.setText(_translate("Dialog", "Time zone"))
        self.ispCheckBox.setToolTip(_translate("Dialog", "<html><head/><body><p>The IP user Internet Service Provider.</p><p><br/></p><p>Examples: Mobin Net Communication Company, SURFnet II c.</p></body></html>"))
        self.ispCheckBox.setText(_translate("Dialog", "ISP"))
        self.latitudeCheckBox.setToolTip(_translate("Dialog", "<html><head/><body><p>The IP user Internet Service Provider.</p><p><br/></p><p>Examples: Mobin Net Communication Company, SURFnet II c.</p></body></html>"))
        self.latitudeCheckBox.setText(_translate("Dialog", "latitude"))
        self.longitudeCheckBox.setToolTip(_translate("Dialog", "<html><head/><body><p>The IP user Internet Service Provider.</p><p><br/></p><p>Examples: Mobin Net Communication Company, SURFnet II c.</p></body></html>"))
        self.longitudeCheckBox.setText(_translate("Dialog", "Longitude"))
        self.label_4.setText(_translate("Dialog", "   Connection Status"))


class NyvoNetHunterApp(QDialog):

    fill_animationgroup_finished = pyqtSignal()
    setted_examine_attributes = pyqtSignal()
    examine_options_satisfied = pyqtSignal()
    connectable_is_generated = pyqtSignal()
    invalid_endpoint_passed = pyqtSignal()
    no_examine_option_found = pyqtSignal()
    progressbar_is_filled = pyqtSignal()
    user_input_is_empty = pyqtSignal()

    cant_spoof_location = pyqtSignal()
    can_spoof_location = pyqtSignal()
    longitude_found = pyqtSignal()
    latitude_found = pyqtSignal()

    network_query_finished = pyqtSignal()

    inputted_text = ""

    def set_progressbar_value(self, amount: int) -> None:
    
        if amount > 100:
            raise TypeError(f"The progress bar fill amount cannot be more than 100.")

        if not isinstance(amount, (int, float)):
            amount_argument_type = type(amount).__name__
            raise TypeError(
                f"Expected argument type for the parameter ( amount ): int | Not {amount_argument_type}"
            )

        self.ui.progressBar.setValue(amount)
    
    def _set_examine_attributes(self, connectable: Connectable) -> str:
    
        api_key = "KBvhRDGVffUsQQ97m1Cm6SkmBERj8NLXPqZH8A0y"
        ip_lookup_api_url = "http://ip-api.com/json/"
        url_lookup_api_url = "https://api.api-ninjas.com/v1/urllookup?url="

        if not isinstance(connectable, Connectable):
            connectable_argument_type = type(connectable).__name__
            raise ValueError(
            f"Expected argument type passed for the parameter ( connectable ): Connectable | Not: ( {connectable_argument_type} )"
            )

        try:
            connectable_endpoint_type = find_endpoint_type(connectable=connectable)

        except (TypeError, ValueError) as exception:
            error_type = type(exception)
            error_message = repr(exception)

            raise error_type(error_message)

        api_key_sign = "X-Api-Key"
        api_key_value = api_key
        api_key_header = {api_key_sign: api_key_value}
        
        self.network_manager_worker.__setattr__("headers", api_key_header)
        self.network_manager_worker.__setattr__("data", {})
        self.network_manager_worker.__setattr__("method", "get")
        

        if connectable_endpoint_type == "ip":
            self.network_manager_worker.__setattr__("url", f"{ip_lookup_api_url}{connectable.endpoint}")
            self.setted_examine_attributes.emit()
            return

        if connectable_endpoint_type == "url":
            self.network_manager_worker.__setattr__("url", f"{url_lookup_api_url}{connectable.endpoint}")
            self.setted_examine_attributes.emit()
            return
        
    def generate_user_desired_connectable(self) -> Connectable:
        self.ui.responseLabel.clear()
    
        self.inputted_text = self.ui.lineEdit.text()
        line_edit_is_empty = not self.inputted_text
        if line_edit_is_empty:
            self.user_input_is_empty.emit()
            return 
        
        try:
        
            generated_connectable = generate_valid_connectable(self.inputted_text)
             
        except (ValueError, TypeError):
            self.invalid_endpoint_passed.emit()
            return
            
        self.generated_connectable = generated_connectable
            
            
        self.connectable_is_generated.emit()
        return generated_connectable
    
        
    def show_response(self) -> None:

        self.bool_latitude_found = False
        self.bool_longitude_found = False

        self.latitude = 1
        self.longitude = 1

        response = self.network_manager_worker.response.json()

        self.checked_options = self.get_checked_examine_options()
        self.checked_options_amount = len(self.checked_options)
        
        self.unfetched_options_count = 0
        self.examine_text = ""
        for option_index, option in enumerate(self.checked_options):
            option_index = option_index + 1

            try:    

                if not response[option]:
                    raise KeyError("...")
            
                self.examine_text += f"{option_index}. {option}: {response[option]}.\n"

                if option == "lon":
                    self.longitude = float(response[option])

                    self.bool_longitude_found = True
                    self.longitude_found.emit()

                if option == "lat":
                    self.latitude = float(response[option])

                    self.bool_latitude_found = True
                    self.latitude_found.emit()
            
            except KeyError:
                self.unfetched_options_count += 1
                self.examine_text += f"{option_index}. {option}: Not found.\n"

        
        if self.unfetched_options_count == self.checked_options_amount:
            self.examine_text = "No checked option found."
        
        self.examine_text += f"\n\nExamined endpoint: {self.inputted_text}"
        
        self.ui.responseLabel.setText(self.examine_text)
        self.ui.lineEdit.clear()

        self.network_query_finished.emit()
        return
        
    def api_connected_animation(self) -> None:
        self.progressbar_percent_animation = QPropertyAnimation(targetObject=self.ui.progressBar, propertyName="value".encode(), parent=self)
        
        self.progressbar_percent_animation.setDuration(1000)
        self.progressbar_percent_animation.setStartValue(0)
        self.progressbar_percent_animation.setEndValue(100)
        
        self.ui.callstatusLabel.setText("Connecting...")
        
        self.progressbar_percent_animation.start()
        
        self.progressbar_percent_animation.finished.connect(self.fill_animationgroup_finished.emit)
        
    def api_disconnected_animation(self) -> None:
        selfprogressbar_percent_animation = QPropertyAnimation(targetObject=self.ui.progressBar, propertyName="value".encode(), parent=self)
        
        selfprogressbar_percent_animation.setDuration(1000)
        selfprogressbar_percent_animation.setStartValue(100)
        selfprogressbar_percent_animation.setEndValue(0)
        
        self.ui.callstatusLabel.setText("Diconnected...") 
            
    def api_examining_animation(self) -> None:
        self.progressbar_percent_animation = QPropertyAnimation(targetObject=self.ui.progressBar, propertyName="value".encode( ), parent=self)
        
        self.progressbar_percent_animation.setDuration(20000)
        self.progressbar_percent_animation.setStartValue(0)
        self.progressbar_percent_animation.setEndValue(100)
        self.ui.callstatusLabel.setText("Examining...")

        self.progressbar_percent_animation.start()

    def api_responded_animation(self) -> None:
        self.progressbar_percent_animation = QPropertyAnimation(targetObject=self.ui.progressBar, propertyName="value".encode(), parent=self)
        
        self.progressbar_percent_animation.setDuration(500)
        self.progressbar_percent_animation.setStartValue(100)
        self.progressbar_percent_animation.setEndValue(0)
        
        self.progressbar_percent_animation.start()
        self.ui.callstatusLabel.setText("Awaiting...")
        
    def api_fast_fill_animation(self) -> None:
        self.progressbar_percent_animation = QPropertyAnimation(targetObject=self.ui.progressBar, propertyName="value".encode(), parent=self)
        
        self.progressbar_percent_animation.setDuration(100)
        self.progressbar_percent_animation.setStartValue(self.ui.progressBar.value())
        self.progressbar_percent_animation.setEndValue(100)
        
        self.progressbar_percent_animation.start()
        self.ui.callstatusLabel.setText("Examining...")
        
        self.fill_animationgroup_finished.emit()
        
    def api_kill_animation(self):
        self.progressbar_percent_animation.stop()

        self.ui.callstatusLabel.setText("Awaiting...")
        self.ui.progressBar.setValue(0)

    def get_checked_examine_options(self) -> [list, None]:
        self.bool_longitude_found = False
        self.bool_latitude_found = False
        
        all_options = [option for option in dir(self.ui) if option.endswith("CheckBox")]
        requested_options = [getattr(self.ui, option) for option in all_options]
        self.checked_options_list = [option.objectName().replace("CheckBox", "") for option in requested_options if option.isChecked()]
        
        for option in self.checked_options_list:
            option_index = self.checked_options_list.index(option)

            if option == "zipcode":
                unified_option = option.replace("zipcode", "zip")    
                self.checked_options_list.insert(option_index, unified_option)

                del self.checked_options_list[option_index+1]
                
            if option == "latitude":
                unified_option = option.replace("latitude", "lat")
                self.checked_options_list.insert(option_index, unified_option)
                
            
                del self.checked_options_list[option_index+1]
                
            elif option == "longitude":
                unified_option = option.replace("longitude", "lon")
                self.checked_options_list.insert(option_index, unified_option)

                del self.checked_options_list[option_index+1]
                
        if not self.checked_options_list:
            self.no_examine_option_found.emit()
            return self.checked_options_list
        
        if self.checked_options_list:
            self.checked_options_list.sort()

        caller_function = inspect.currentframe().f_back.f_code.co_name
        if not caller_function == "show_response":
            self.examine_options_satisfied.emit()

        return self.checked_options_list
        
    def no_connection_state(self) -> None:
    
        check_boxes = [
        
        widget for widget in dir(self.ui) 
        if not widget.startswith("__") 
        and not widget.endswith("__") 
        and widget.endswith("CheckBox")

        ]
    
        self.ui.lineEdit.clear()
        self.ui.lineEdit.setDisabled(True)
        self.ui.pushButton.setDisabled(True)
        self.ui
        
        for check_box in check_boxes:
            eval(f"self.ui.{check_box}.setDisabled(True)")
            
        self.ui.responseLabel.setText("No internet connection.")
        self.ui.connection_status_label.setPixmap(self.ui.no_connection_icon)

    def warning_request_timeout(self) -> None:
        self.ui.responseLabel.setText("Request timed out, please try again.")

    def examining_state(self) -> None:
        self.ui.pushButton.setDisabled(True)
        self.ui.pushButton.setText(None)

        self.ui.lineEdit.setDisabled(True)

        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(
                "main_program/source/ui_design/resources/pictures/check_mark.png"
            ),
            QtGui.QIcon.Normal,
            QtGui.QIcon.On,
        )
        self.ui.pushButton.setIcon(icon1)

    def default_query_state(self) -> None:
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton.setText("Examine")

        self.ui.lineEdit.setEnabled(True)

        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(
                "main_program/source/ui_design/resources/pictures/pushbuttonicon.png"
            ),
            QtGui.QIcon.Normal,
            QtGui.QIcon.On,
        )
        self.ui.pushButton.setIcon(icon1)

    def connected_state(self) -> None:  
    
        check_boxes = [
        
        widget for widget in dir(self.ui) 
        if not widget.startswith("__") 
        and not widget.endswith("__") 
        and widget.endswith("CheckBox")

        ]
        
        self.ui.lineEdit.clear()
        self.ui.lineEdit.setEnabled(True)
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton.setEnabled(True)

        for check_box in check_boxes:
            eval(f"self.ui.{check_box}.setDisabled(False)")
            
        self.ui.responseLabel.clear()
        
        self.ui.connection_status_label.setPixmap(self.ui.connected_icon)

    def web_view_default_state(self) -> None:
        project_root_directory = Path.cwd()
        self.base_state_html = QtCore.QUrl.fromLocalFile(
            f"{project_root_directory}/main_program/source/coding/database/map_api/data_storage/base_state.html"
        )

        self.ui.webView.load(self.base_state_html)
        
    def initialize_connection_checker(self) -> None:
        self.connection_status_thread = QThread()
        self.connection_status_worker = ConnectionStatusChecker()

        self.connection_status_worker.lost_connection.connect(self.no_connection_state)
        self.connection_status_worker.spotted_connection.connect(self.connected_state)

        self.connection_status_worker.moveToThread(self.connection_status_thread)
        self.connection_status_thread.started.connect(self.connection_status_worker.run)

        self.connection_status_thread.start()

    def initialize_network_logic(self) -> None:
        self.ui.lineEdit.textChanged.connect(self.get_input_text)

        self.network_manager_worker = NyvoNetHunterRequestManager(url="https://github.com/KhodeNima", data={}, headers={}, method="get")
        self.network_manager_thread = QThread()

        self.network_manager_worker.moveToThread(self.network_manager_thread)
        self.network_manager_thread.started.connect(self.network_manager_worker.fire)
        self.examine_options_satisfied.connect(self.generate_user_desired_connectable)

        self.connectable_is_generated.connect(lambda: self._set_examine_attributes(self.generated_connectable))
    
        self.user_input_is_empty.connect(lambda: self.ui.responseLabel.setText("Please provide a valid IP or URL address."))
        self.invalid_endpoint_passed.connect(lambda: self.ui.responseLabel.setText(f"{self.simplified_input} is not a valid IP or URL address."))
        self.no_examine_option_found.connect(lambda: self.ui.responseLabel.setText("Please choose at least 1 examine option."))

        self.network_manager_worker.received_valid_response.connect(self.show_response)
        self.network_manager_worker.received_invalid_response.connect(self.show_response)
        self.network_manager_worker.received_invalid_response.connect(self.network_manager_thread.exit)
        self.network_manager_worker.received_valid_response.connect(self.network_manager_thread.exit)

        self.network_manager_worker.failed_to_send.connect(self.warning_request_timeout)
        self.network_manager_worker.failed_to_send.connect(self.network_manager_thread.exit)

        self.setted_examine_attributes.connect(self.network_manager_thread.start)

        self.ui.pushButton.clicked.connect(self.get_checked_examine_options)

    def initialize_spoofer_logic(self) -> None:
        self.map_spoofer = MapSpoofer(0, 0)
        self.html_data_storage = "main_program/source/coding/database/map_api/data_storage/spoof_result.html"

        check_spoof_status = lambda: (self.can_spoof_location.emit() 
            if all([self.bool_latitude_found, self.bool_longitude_found]) else self.cant_spoof_location.emit()
        )

        self.network_query_finished.connect(check_spoof_status)

        self.cant_spoof_location.connect(self.web_view_default_state)

        self.network_query_finished.connect(check_spoof_status)

        self.can_spoof_location.connect(lambda: self.map_spoofer.set_latitude(self.latitude))
        self.can_spoof_location.connect(lambda: self.map_spoofer.set_longitude(self.longitude))
        self.can_spoof_location.connect(self.map_spoofer.start)

        self.map_spoofer.location_spoofed.connect(lambda: self.map_spoofer.save_as_html_file(self.html_data_storage))

        project_root_directory = Path.cwd()
        map_location_file_path = QtCore.QUrl.fromLocalFile(
            f"{project_root_directory}/main_program/source/coding/database/map_api/data_storage/spoof_result.html"
        )

        self.map_spoofer.saved_as_html.connect(lambda: self.ui.webView.load(map_location_file_path))


    def initialize_animations_logic(self) -> None:
        self.web_view_default_state()

        self.connection_status_worker.lost_connection.connect(self.web_view_default_state)

        self.fill_animationgroup_finished.connect(self.api_kill_animation)

        self.network_manager_worker.request_started.connect(self.api_examining_animation)
        self.network_manager_worker.request_sent.connect(self.api_responded_animation)

        self.network_manager_worker.received_valid_response.connect(self.api_responded_animation)
        self.network_manager_worker.received_invalid_response.connect(self.api_responded_animation)

        self.network_manager_worker.failed_to_send.connect(self.warning_request_timeout)
        self.network_manager_worker.failed_to_send.connect(self.api_responded_animation)

        self.network_manager_worker.request_started.connect(self.examining_state)
        self.network_manager_worker.request_sent.connect(self.default_query_state)

    def get_input_text(self) -> str:
        self.inputted_text = self.ui.lineEdit.text()
        self.simplified_input = simplify_long_string(self.inputted_text)

        return self.inputted_text
    

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
    
        self.initialize_network_logic()
        self.initialize_connection_checker()
        self.initialize_animations_logic()
        self.initialize_spoofer_logic()
        self.show()
        
  
if __name__ == "__main__":
    app = QApplication(sys.argv + ["--no-sandbox"])
    app_window = NyvoNetHunterApp()

    app_window.show()
    sys.exit(app_window.exec_())