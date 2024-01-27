#!/usr/bin/env python3
"""
# The unit test module for ip validation functions in the ( data.py ) module.
"""


def setup_database_import_path() -> None:
    from sys import path as module_paths
    import pathlib

    project_root_directory = pathlib.Path.cwd()

    module_paths.append(f"{project_root_directory}/main_program/source/coding")
    module_paths.append(f"{project_root_directory}/main_program/source/coding/database")


setup_database_import_path()


import unittest
from unittest import TestCase
from unittest.result import TestResult
from database.workers.api import (
    is_valid_ip,
    is_valid_ipv4,
    is_valid_ipv6,
)


class TestIpValidators(TestCase):
    def setUp(self) -> None:
        self.valid_ipv4_1 = "120.121.122.123"
        self.valid_ipv4_2 = "151.152.153.154"

        self.valid_ipv6_1 = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
        self.valid_ipv6_2 = "20cf:42f3:505b:508d:e2d9:0cf7:91de:fc1b"

        self.invalid_ip = "I'm not an IP!"

    def test_ip_validator(self) -> unittest.result:
        self.assertTrue(is_valid_ip(self.valid_ipv4_1))
        self.assertTrue(is_valid_ip(self.valid_ipv6_1))

        self.assertFalse(is_valid_ip(self.invalid_ip))

    def test_ipv4_validator(self) -> unittest.result:
        self.assertTrue(is_valid_ipv4(self.valid_ipv4_1))
        self.assertTrue(is_valid_ipv4(self.valid_ipv4_2))

        self.assertFalse(is_valid_ipv4(self.invalid_ip))

        self.assertFalse(is_valid_ipv4(self.valid_ipv6_1))
        self.assertFalse(is_valid_ipv4(self.valid_ipv6_2))

    def test_ipv6_validator(self) -> unittest.result:
        self.assertTrue(is_valid_ipv6(self.valid_ipv6_1))
        self.assertTrue(is_valid_ipv6(self.valid_ipv6_2))

        self.assertFalse(is_valid_ipv6(self.invalid_ip))

        self.assertFalse(is_valid_ipv6(self.valid_ipv4_1))
        self.assertFalse(is_valid_ipv6(self.valid_ipv4_2))


module_is_runned_directly = __name__ == "__main__"
if module_is_runned_directly:
    unittest.main()
