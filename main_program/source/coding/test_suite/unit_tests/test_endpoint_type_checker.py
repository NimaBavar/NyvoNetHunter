#!/usr/bin/env python3
"""
# The unit test module for ( find_endpoint_type ) function in ( data.py ) module.
"""


def setup_database_import_path() -> None:
    from sys import path as module_paths
    import pathlib

    project_root_directory = pathlib.Path.cwd()

    module_paths.append(f"{project_root_directory}/main_program/source/coding/database")
    module_paths.append(f"{project_root_directory}/main_program/source/coding")


setup_database_import_path()


import unittest
from unittest import TestCase
from unittest.result import TestResult
from database.workers.api import (
    NyvoNetHunterIpAddress,
    NyvoNetHunterUrl,
    find_endpoint_type,
)


class TestEndpointTypeChecker(TestCase):
    def setUp(self) -> None:
        self.valid_ip_connectable_1 = NyvoNetHunterIpAddress("144.145.146.147")
        self.valid_ip_connectable_2 = NyvoNetHunterIpAddress("178.179.190.140")

        self.valid_url_connectable_1 = NyvoNetHunterUrl("github.com")
        self.valid_url_connectable_2 = NyvoNetHunterUrl("https://discord.com")
        self.valid_url_connectable_3 = NyvoNetHunterUrl("https://github.com/KhodeNima")

        self.invalid_endpoint_1 = "I AM AN INVALID ENDPOINT!"

    def test_invalid_endpoint_type(self) -> TestResult:
        self.assertRaises(TypeError, find_endpoint_type, args=self.invalid_endpoint_1)

    def test_url_endpoint_type(self) -> TestResult:
        self.assertEqual(find_endpoint_type(self.valid_url_connectable_1), "url")
        self.assertEqual(find_endpoint_type(self.valid_url_connectable_2), "url")
        self.assertEqual(find_endpoint_type(self.valid_url_connectable_3), "url")

    def test_ip_endpoint_type(self) -> TestResult:
        self.assertEqual(find_endpoint_type(self.valid_ip_connectable_1), "ip")
        self.assertEqual(find_endpoint_type(self.valid_ip_connectable_2), "ip")


module_is_runned_directly = __name__ == "__main__"
if module_is_runned_directly:
    unittest.main()
