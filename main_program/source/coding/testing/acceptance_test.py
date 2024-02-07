#!/usr/bin/env python3
"""
# The application full acceptance test.

! Do not Attempt to run this module directly, use the unittest package instead.
"""


def setup_database_import_path() -> None:
    from sys import path as module_paths
    import pathlib

    project_root_directory = pathlib.Path.cwd()

    module_paths.append(f"{project_root_directory}/main_program/source/coding")
    module_paths.append(f"{project_root_directory}/main_program/source/coding/database")
    module_paths.append(f"{project_root_directory}/main_program/source/coding/database/workers")


setup_database_import_path()


import sys
import warnings
import unittest
from unittest.result import TestResult
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from pyperclip import paste
from database.gui_setup.gui_logic import NyvoNetHunterApp


def handle_object_conflicts(exc_type, exc_value, traceback) -> None:
    warnings.filterwarnings("ignore", category=FutureWarning)
    if exc_type is RuntimeError:
        return

    raise exc_type(f"{exc_value}: {traceback}")


sys.excepthook = handle_object_conflicts
app = QApplication([])


class TestCopyButton(unittest.TestCase):
    def setUp(self) -> None:
        self.app_window = NyvoNetHunterApp()

        self.app_window.ui.ispCheckBox.setChecked(True)
        self.valid_connectable = "github.com"

    def test_copy_button_disabled(self) -> TestResult:
        self.app_window.ui.lineEdit.setText("I'm an invalid connectable!")
        QTest.mouseClick(self.app_window.ui.searchButton, Qt.MouseButton.LeftButton)

        self.assertFalse(self.app_window.ui.copyButton.isEnabled())

    def test_copy_button_enabled(self) -> TestResult:
        self.app_window.ui.lineEdit.setText("github.com")

        self.assertTrue(self.app_window.ui.copyButton.isEnabled())

    def test_copy_button_text_change(self) -> TestResult:
        self.app_window.ui.lineEdit.setText(self.valid_connectable)
        QTest.mouseClick(self.app_window.ui.copyButton, Qt.MouseButton.LeftButton)

        self.assertEqual(self.app_window.ui.copyButton.text(), "Result copied to clipboard.")

    def test_clipboard_interaction(self) -> TestResult:
        self.app_window.ui.lineEdit.setText(self.valid_connectable)
        self.app_window.ui.responseLabel.setText("Testing.")
        QTest.mouseClick(self.app_window.ui.copyButton, Qt.MouseButton.LeftButton)

        self.assertEqual(self.app_window.ui.responseLabel.text(), paste())


if __name__ == "__main__":
    unittest.main()
