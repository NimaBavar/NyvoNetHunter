#!/usr/bin/env python3
"""
# The app requirements installer module.
"""


from os import system as cmd_input 
from time import sleep
    

def install_all_requirements():

    cmd_input("echo installing first-time run requirements, please wait...")
    sleep(3)

    with open("main_program/source/coding/database/post_launch_data/requirements.txt", "r") as requirements_list:
        for requirement in requirements_list:
            cmd_input("python.exe -m pip install --upgrade pip")
            cmd_input(f"pip install {requirement}")