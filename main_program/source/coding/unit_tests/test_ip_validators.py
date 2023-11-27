#!/usr/bin/env python3
"""
The unit test module for ip validation functions in the ( data.py ) file.
"""

import sys
sys.path.append("..")

from database.data import (
    is_valid_ip, 
    is_valid_ipv4, 
    is_valid_ipv4,
)
from unittest import TestCase
import unittest


class TestIpValidations(TestCase):

    def setUp(self) -> None:
    
        self.valid_ipv4 = "120.121.122.123"
        self.valid_ipv6 = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
    
        self.invalid_ipv4 = "I'm not an Ipv4."
        self.invalid_ipv4 = "I'm not an Ipv6."
    
    def test_valid_ip_check(self):
    
        self.assertTrue(is_valid_ip, self.valid_ipv4)
        
        