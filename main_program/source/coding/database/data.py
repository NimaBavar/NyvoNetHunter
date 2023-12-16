"""
# The base data file of the project
---
"""


def setup_database_import_path() -> None:
    from sys import path as module_paths
    import pathlib

    project_root_directory = pathlib.Path.cwd()

    module_paths.append(f"{project_root_directory}/main_program/source/coding")
    module_paths.append(f"{project_root_directory}/main_program/source/coding/database")


setup_database_import_path()


from exceptions.direct_run_error import DirectRunError
from packages import (
    cmd_input,
    platform,
)


__version__ = "6.2.5"
__author__ = "KhodeNima ( Nima Bavar )"
__build_date__ = "2023/11/13"


def clean_terminal() -> None:
    runner_operating_system = platform(terse=True)
    operating_system_is_windows = runner_operating_system.lower().startswith("windows")
    operating_system_is_linux = runner_operating_system.lower().startswith("linux")
    
    if operating_system_is_windows:
        cmd_input("cls")
        return
        
    if operating_system_is_linux:
        cmd_input("clear")
        

module_is_runned_directly = __name__ == "__main__"

if module_is_runned_directly:
    clean_terminal()
    raise DirectRunError(
        "Database modules are not intended to run directly. They are produced for import usage only."
    )
