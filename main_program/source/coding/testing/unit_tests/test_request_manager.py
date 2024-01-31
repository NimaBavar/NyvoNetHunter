#!/usr/bin/env python3::
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


import unittest
from unittest import mock
from unittest.result import TestResult
from database.workers.api import NyvoNetHunterRequestManager
from database.workers import api


class TestRequestManager(unittest.TestCase):
    def setUp(self) -> None:
        self.invalid_http_method = "kill"
        self.response_validation_request_manager = NyvoNetHunterRequestManager(url="https://github.com", data={}, headers={}, method="get")

    def test_invalid_url(self) -> TestResult:
        with self.assertRaises(TypeError):
            NyvoNetHunterRequestManager(url="I am not a real URL.", data={}, headers={}, method="get")

    def test_invalid_method(self) -> TestResult:
        with self.assertRaises(ValueError):   
            NyvoNetHunterRequestManager(url="https://github.com", data={}, headers={}, method=3)

        with self.assertRaises(TypeError):
            NyvoNetHunterRequestManager(url="https://github.com", data={}, headers={}, method=self.invalid_http_method)
        
    def test_invalid_data(self) -> TestResult:
        with self.assertRaises(ValueError):
            NyvoNetHunterRequestManager(url="https://github.com", data=3, headers={}, method="get")
            NyvoNetHunterRequestManager(url="https://github.com", data=True, headers={}, method="get")

    def test_schemeless_url(self) -> TestResult:
        try:
            NyvoNetHunterRequestManager(url="github.com", data={}, headers={}, method="get")

        except AssertionError:
            self.fail(f"Testing schemeless URLs: Failed.")
    
    @mock.patch.object(NyvoNetHunterRequestManager, "failed_to_send")
    def test_failed_connection_state(self, _mock_failed_to_send_signal) -> TestResult:
        request_manager = NyvoNetHunterRequestManager(url="https://github.com", data={}, headers={}, method="get")
        _mock_failed_to_send_signal.emit = mock.Mock()


        with mock.patch("database.workers.api.requests.request") as request_mock:
            request_mock.side_effect = AssertionError("Could not connect to service.")

            self.assertRaises(Exception, request_manager.fire)
            _mock_failed_to_send_signal.emit.assert_called()
    
    def test_received_valid_response_state(self) -> TestResult:
        self.response_validation_request_manager.response = mock.Mock()
        self.response_validation_request_manager.response.ok = True

        self.assertTrue(self.response_validation_request_manager.check_response_is_valid())

    def test_received_invalid_response_state(self) -> TestResult:
        self.response_validation_request_manager.response = mock.Mock()
        self.response_validation_request_manager.response.ok = False

        self.assertFalse(self.response_validation_request_manager.check_response_is_valid())


if __name__ == "__main__":
    unittest.main()
