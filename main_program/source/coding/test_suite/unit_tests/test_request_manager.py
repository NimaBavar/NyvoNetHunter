#!/usr/bin/env python3
"""
# The main unittest module for the NyvoNetHunterRequestManager class.
"""


def setup_database_import_path() -> None:
    from sys import path as module_paths
    import pathlib

    project_root_directory = pathlib.Path.cwd()

    module_paths.append(f"{project_root_directory}/main_program/source/coding")
    module_paths.append(f"{project_root_directory}/main_program/source/coding/database")

setup_database_import_path()


from typing import Type
import unittest
from unittest.result import TestResult
from database.workers.api import NyvoNetHunterRequestManager


class TestRequestManager(unittest.TestCase):

    def test_invalid_url(self) -> TestResult:
        with self.assertRaises(TypeError):
            NyvoNetHunterRequestManager(url="I am not a real URL.", data={}, headers={}, method="get")

    def test_invalid_method(self) -> TestResult:
        with self.assertRaises(ValueError):   
            NyvoNetHunterRequestManager(url="https://github.com", data={}, headers={}, method=3)

        with self.assertRaises(TypeError):
            NyvoNetHunterRequestManager(url="https://github.com", data={}, headers={}, method="kill")
        
    def test_invalid_data(self) -> TestResult:
        with self.assertRaises(ValueError):
            NyvoNetHunterRequestManager(url="https://github.com", data=3, headers={}, method="get")
            NyvoNetHunterRequestManager(url="https://github.com", data=True, headers={}, method="get")

    def test_schemeless_url(self) -> TestResult:
        try:
            NyvoNetHunterRequestManager(url="github.com", data={}, headers={}, method="get")

        except AssertionError:
            self.fail(f"Testing schemeless URLs: Failed.")


if __name__ == "__main__":
    unittest.main()
