#!/usr/bin/env python3
"""
# The module for testing the ( `NyvoNetHunterUrl` ) class.

Note that this test case does not test the url validators of the class, as their existence
in this class is the result of composition, they are tested in test cases of their own.
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
        self.url_with_path = NyvoNetHunterUrl("https://hello.com/how/are/you.com")

    def test_invalid_url_type(self) -> TestResult:
        with self.assertRaises(ValueError):
            NyvoNetHunterUrl(3)

    def test_path_remover(self) -> None:
        path_removed_url = self.url_with_path.remove_paths()
        self.assertEqual(path_removed_url, "https://hello.com")


if __name__ == "__main__":
    unittest.main()
