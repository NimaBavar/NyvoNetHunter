#!/usr/bin/env python3
"""
# The main module for the port scanning operations.
"""


def setup_database_import_path() -> None:
    from sys import path as module_paths
    import pathlib
    

    project_root_directory = pathlib.Path.cwd()

    module_paths.append(f"{project_root_directory}/main_program/source/coding/database")
    module_paths.append(f"{project_root_directory}/main_program/source/coding")

setup_database_import_path()


from typing import Literal
from database.packages import ( 
    NmapParser,
    NmapProcess,
    NmapReport,
    sleep,
) 
from database.packages import pyqtSignal
from database.packages import QObject
from database.workers.api import NyvoNetHunterUrl, NyvoNetHunterIpAddress, Connectable
from database.exceptions.direct_run_error import DirectRunError
from database.exceptions.port_scanner_exceptions.no_scan_history import NoScanHistoryError


class NyvoNetHunterPortScanner(QObject):
    open_port_found = pyqtSignal()
    open_port_not_found = pyqtSignal()
    _bool_scan_finished = False

    scan_started = pyqtSignal()
    scan_finished = pyqtSignal()
    scan_failed = pyqtSignal()

    scan_stopped = pyqtSignal()
    

    def __init__(self, connectable: Connectable):
        """
        The base class for the Nmap port scanning feature.

        Parameters
        ----------
        connectable | Connectable
            The connectable that its endpoint is to be scanned.
        """
        self.connectable = connectable
        self._scan_attempts = 0

        super(QObject, self).__init__()

    def scan(self, timeout: int=10) -> int:
        """
        Starts the Nmap scan.

        Parameters
        ----------
        timeout | int, default = 1
            The timeout ( seconds ) for the scanner ( Cannot be more than 40 ) to stop o to stop on.

        Returns
        -------
        int
            The Nmap launch code ( error code unless 0 ).
        """
        if not isinstance(timeout, int):
            argument_type = type(timeout).__name__
            raise ValueError(f"Expected argument type passed for the parameter ( timeout ): ( int ) | Not: ( {argument_type} )")
        
        if timeout > 40:
            raise TypeError("The timeout amount cannot be more than 40.")

        self._scanner.run()
        self.scan_started.emit()

        elapsed_seconds = 0
        while self._scanner.is_running():
            if elapsed_seconds == timeout:
                self._scanner.stop()

                self.scan_stopped.emit()
                return 0

            sleep(1)
            elapsed_seconds += 1
        
        if self._scanner.has_failed():
            self.scan_failed.emit()
            self.scan_result = self._scanner.summary


        self._scan_attempts += 1
        
        self.scan_finished.emit()
        self._unformatted_scan_result = self._scanner.stdout
        
        self.scan_result = self.__class__._parse_scan_result(self._scanner.stdout)
        self._bool_scan_finished = True
        
        nmap_return_code = self._scanner.rc
        return nmap_return_code

    def get_scan_data(self, data: Literal["open_ports"]="open_ports") -> list:
        """
        Retrieves a specific data from the scan result.

        Parameters
        -------
        data : { "open_ports" }, default="open_ports"
            The data to grep from the scan.

        Returns
        -------
        list
            The data look_up result.

        Raises
        -------
        NoScanHistoryError
            If the look_up was attempted before a valid scanself.
        TypeError
            If the provided data is not valid.
        """
        valid_datas = ["open_ports"]

        successful_scan_not_occured = self._scan_attempts == 0 or not self._bool_scan_finished or not self._scanner.rc == 0
        if successful_scan_not_occured:
            raise NoScanHistoryError("Please scan at least 1 host in order to receive the open ports.")

        if not data in valid_datas:
            raise TypeError(f"{data} is not a valid/or and existing scan data.")


        hosts = [host for host in self.scan_result.hosts]

        if data == "open_ports":
            open_ports = [f"{host.ipv4}: {host.get_open_ports()}" if host.is_up() else f"{host.ipv4}: host is down." for host in hosts]
            retrieved_scan_data = open_ports


        return retrieved_scan_data

    @classmethod
    def _parse_scan_result(cls, result_to_format: str) -> NmapReport:
        """
        Parse the XML results of a Nmap scan to a accessible class.


        Parameters
        ----------
        cls
            The class name ( NyvoNetHunterPortScanner ).
        result_to_format | str
            The Nmap XML result.

        Returns
        -------
        NmapReport
            Accessible libnmap.objects.NmapReport object.
        """
        parser = NmapParser()
        parse_result = parser.parse(result_to_format)

        return parse_result

    @property
    def connectable(self) -> str | Connectable:
        return self._connectable

    @connectable.setter
    def connectable(self, connectable: Connectable) -> None:
        if not isinstance(connectable, (Connectable)):
            argument_type = type(connectable).__name__
            raise ValueError(f"Expected argument type passed for the parameter ( connectable ): ( Connectable ) | Not: ( {argument_type} ).")


        self._connectable = connectable
        self._formatted_connectable_endpoint = self._connectable.endpoint

        if isinstance(self._connectable, NyvoNetHunterUrl):
            self._formatted_connectable_endpoint = NyvoNetHunterUrl(self._connectable.remove_suffix(apply_to_endpoint=False))
            self._formatted_connectable_endpoint = self._formatted_connectable_endpoint.remove_paths(apply_to_endpoint=False)
        
        self._scanner = NmapProcess(self._formatted_connectable_endpoint)


scanner = NyvoNetHunterPortScanner(NyvoNetHunterUrl("github.com"))
scanner.scan_started.connect(lambda: print("scan started."))

scanner.scan(timeout=-1)
