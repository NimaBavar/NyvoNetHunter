"""
# The informational module of the project.
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
from workers.api import clean_terminal
from packages import dataclass


@dataclass
class BuildData:
    __version__ = "9.5.8"
    __author__ = "KhodeNima ( Nima Bavar )"
    __build_date__ = "2023/11/13"


module_is_runned_directly = __name__ == "__main__"
if module_is_runned_directly:
    clean_terminal()
    raise DirectRunError(
        "Database modules are not intended to run directly. They are produced for import usage only"
    )