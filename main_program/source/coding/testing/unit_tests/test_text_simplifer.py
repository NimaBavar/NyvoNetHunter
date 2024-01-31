#!/usr/bin/env python3
"""
The unittest module for the text simplifier function.
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
from database.workers.api import simplify_text


class TestTextSimplifier(unittest.TestCase):
    def setUp(self) -> None:
        self.long_string1 = "HelloI'mAlex"
        self.long_string2 = "MyNameIsAlex"

        self.short_string1 = "Hi"
        self.short_string2 = "Bye"

    def test_long_text_response(self) -> TestResult:
        self.assertEqual(simplify_text(self.long_string1), "HelloI...")
        self.assertEqual(simplify_text(self.long_string2), "MyName...")

    def test_short_text_response(self) -> TestResult:
        self.assertEqual(simplify_text(self.short_string1), "Hi")
        self.assertEqual(simplify_text(self.short_string2), "Bye")



module_is_runned_directly = __name__ == "__main__"
if module_is_runned_directly:
    unittest.main()
