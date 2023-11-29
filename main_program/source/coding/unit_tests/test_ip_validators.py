#!/usr/bin/env python3
"""
The unit test module for ip validation functions in the ( data.py ) module.
"""


def setup_database_import_path() -> None:

    import pathlib
    import sys


    current_path_variable = pathlib.Path.cwd()

    sys.path.append(f"{current_path_variable}/main_program/source/coding")
    sys.path.append(f"{current_path_variable}/main_program/source/coding/database")
    
setup_database_import_path()


from database.data import (
    is_valid_ip, 
    is_valid_ipv4, 
    is_valid_ipv6,
)
from unittest import TestCase
import unittest


class TestIpValidators(TestCase):

    def setUp(self) -> None:
    
        self.valid_ipv4_1 = "120.121.122.123"
        self.valid_ipv4_2 = "151.152.153.154"
        
        self.valid_ipv6_1 = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
        self.valid_ipv6_2 = "20cf:42f3:505b:508d:e2d9:0cf7:91de:fc1b"
    
        self.invalid_ip = "I'm not an IP!"
    
    def test_ip_validator(self):
    
        self.assertTrue(is_valid_ip(self.valid_ipv4_1))
        self.assertTrue(is_valid_ip(self.valid_ipv6_1))
        
        self.assertFalse(is_valid_ip(self.invalid_ip))
        
    def test_ipv4_validator(self):
    
        self.assertTrue(is_valid_ipv4(self.valid_ipv4_1))
        self.assertTrue(is_valid_ipv4(self.valid_ipv4_2))
        
        self.assertFalse(is_valid_ipv4(self.invalid_ip))
        
        self.assertFalse(is_valid_ipv4(self.valid_ipv6_1))
        self.assertFalse(is_valid_ipv4(self.valid_ipv6_2))
        
    def test_ipv6_validator(self):
    
        self.assertTrue(is_valid_ipv6(self.valid_ipv6_1))
        self.assertTrue(is_valid_ipv6(self.valid_ipv6_2))
        
        self.assertFalse(is_valid_ipv6(self.invalid_ip))
        
        self.assertFalse(is_valid_ipv6(self.valid_ipv4_1))
        self.assertFalse(is_valid_ipv6(self.valid_ipv4_2))
        

module_is_runned_directly = __name__ == "__main__"

if module_is_runned_directly:
    unittest.main()
    
        