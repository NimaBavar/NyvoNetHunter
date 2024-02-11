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
from database.port_scanner_api.tcp_scanner import NyvoNetHunterPortScanner
