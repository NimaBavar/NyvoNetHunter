"""
# The parrall daemon thread for testing the users internet access
"""


def setup_database_import_path() -> None:
    from sys import path as module_paths
    import pathlib

    project_root_directory = pathlib.Path.cwd()

    module_paths.append(f"{project_root_directory}/main_program/source/coding/database")
    module_paths.append(f"{project_root_directory}/main_program/source/coding")

setup_database_import_path()


from packages import (
    pyqtSignal,
    QObject,
    socket,
)
from exceptions.direct_run_error import DirectRunError


class ConnectionStatusChecker(QObject):
    spotted_connection = pyqtSignal()
    lost_connection = pyqtSignal()

    _timeout = 3
    _host = "8.8.8.8"
    _port = 53

    def start(self):
        """
        Starts the connection checker background daemon.
        """

        self.lost_connection.emit()
        connection_is_available = None

        while True:
            try:
                socket.setdefaulttimeout(__class__._timeout)
                socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((__class__._host, __class__._port))

                if connection_is_available == True:
                    continue

                self.spotted_connection.emit()
                connection_is_available = True

            except socket.error:
                if connection_is_available == False:
                    continue

                self.lost_connection.emit()
                connection_is_available = False

    def is_conneted(self) -> bool:
        """
        Runs a single connection scan and reports it.
        ( Does not run in the background. )

        Returns
        -------
        bool
            Wether the client have a valid internet connection.
        """

        try:
            socket.setdefaulttimeout(__class__._timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((__class__._host, __class__._port))

            return True

        except socket.error:
            return False


module_is_runned_directly = __name__ == "__main__"
if module_is_runned_directly:
    raise DirectRunError(
        "Database modules are not intended to run directly, they are produced for import usage only."
    )
