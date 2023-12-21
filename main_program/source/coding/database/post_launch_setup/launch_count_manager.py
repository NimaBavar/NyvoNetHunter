#!/usr/bin/env python3
"""
# The storage module for the LaunchCountManager class.
"""


from dataclasses import dataclass
import json


@dataclass
class LaunchCountFileInformation:
    file_path = "main_program/source/coding/database/post_launch_data/launch_count.json"


class LaunchCountManager:

    def _load_database_metadata(self):
        with open(LaunchCountFileInformation.file_path, "r") as launch_count_file:
            self.launch_count_dictionary = json.load(launch_count_file)
            
    def _dump_database_metadata(self):
        with open(LaunchCountFileInformation.file_path, "w") as launch_count_file:
            json.dump(self.launch_count_dictionary, launch_count_file)

    def __init__(self):
        self._load_database_metadata()
        self.launch_count = self.launch_count_dictionary["app_launch_count"]
    
    def get_launch_count(self):
        return self.launch_count
    
    def increase_launch_count(self):
        self.launch_count += 1
        return
        
    def store_changes_to_database(self):
        self.launch_count_dictionary["app_launch_count"] = self.launch_count
        self._dump_database_metadata()