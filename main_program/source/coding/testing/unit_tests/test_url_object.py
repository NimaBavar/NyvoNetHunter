#!/usr/bin/env python3
"""
# The module for testing the ( `NyvoNetHunterUrl` ) class.
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
from database.workers.api import NyvoNetHunterUrl


class TestNyvoNetHunterUrl(unittest.TestCase):
    def setUp(self) -> None:
        self.valid_url = NyvoNetHunterUrl("https://github.com")

    def test_invalid_url_type(self) -> TestResult:
        with self.assertRaises(ValueError):
            url = NyvoNetHunterUrl(34)
