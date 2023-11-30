#!/usr/bin/env python3
"""
The unit test module for url validator functions in the ( data.py ) module.
"""

def setup_database_import_path() -> None:

    from sys import path as module_paths
    import pathlib
    
    project_root_directory = pathlib.Path.cwd()
    
    module_paths.append(f"{project_root_directory}/main_program/source/coding/database")
    module_paths.append(f"{project_root_directory}/main_program/source/coding")
    
setup_database_import_path()


from database.data import is_valid_url, clean_terminal
import unittest


class TestUrlValidators(unittest.TestCase):

    def setUp(self) -> None:
        
        self.schemed_valid_url_1 = "https://github.com"
        self.schemed_valid_url_2 = "https://discord.com"
        
        self.noscheme_valid_url_1 = "github.com"
        self.noscheme_valid_url_2 = "discord.com"
        
        self.invalid_url_1 = "I'm not an url!"
        self.invalid_url_2 = "Hello"
        
        
    def test_valid_url_response(self):
    
        self.assertTrue(is_valid_url(self.schemed_valid_url_1))
        self.assertTrue(is_valid_url(self.schemed_valid_url_2))
        
    def test_noscheme_valid_url_response(self):
    
        self.assertTrue(is_valid_url(self.noscheme_valid_url_1))
        self.assertTrue(is_valid_url(self.noscheme_valid_url_2))
    
    def test_invalid_url(self):
    
        self.assertFalse(is_valid_url(self.invalid_url_1))
        self.assertFalse(is_valid_url(self.invalid_url_2))
        

module_is_runned_directly = __name__ == "__main__"

if module_is_runned_directly:
    clean_terminal()
    unittest.main()