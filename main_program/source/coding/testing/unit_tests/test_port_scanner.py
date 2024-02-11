#!/usr/bin/env python3.11
"""
# The module for testing the ( NyvoNetHunterPortScanner ) class.
"""


def setup_database_import_path() -> None:
    from sys import path as module_paths
    import pathlib

    project_root_directory = pathlib.Path.cwd()

    module_paths.append(f"{project_root_directory}/main_program/source/coding")
    module_paths.append(f"{project_root_directory}/main_program/source/coding/database")


setup_database_import_path()


import unittest
from unittest.result import TestResult
from database.port_scanner_api.port_scanner import NyvoNetHunterPortScanner
from database.workers.api import NyvoNetHunterUrl, NyvoNetHunterIpAddress
from database.exceptions.port_scanner_exceptions.no_scan_history import NoScanHistoryError


class TestPortScanner(unittest.TestCase):
    def setUp(self) -> None:
        self.valid_url_connectable = NyvoNetHunterUrl("https://github.com")
        self.valid_port_scanner = NyvoNetHunterPortScanner(self.valid_url_connectable)
            
    def test_invalid_connectable_type(self) -> TestResult:
        with self.assertRaises(ValueError):
            NyvoNetHunterPortScanner(connectable=3)

    def test_data_retrieve_before_scan(self) -> TestResult:
        with self.assertRaises(NoScanHistoryError):
            self.valid_port_scanner.get_scan_data(data="open_ports")

    def test_invalid_data_retrieve(self) -> TestResult:
        with self.assertRaises(TypeError):
            self.valid_port_scanner.get_scan_data(data="rain_diagram")


if __name__ == "__main__":
    unittest.main()
