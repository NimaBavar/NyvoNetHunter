"""
# The parrall daemon thread for testing the user's internet access
"""


from exceptions.direct_run_error import DirectRunError
from packages import (
    ConnectionError,
    pyqtSignal,
    QObject,
    QThread,
    socket,
)


class ConnectionStatusChecker(QObject):
    spotted_connection = pyqtSignal()
    lost_connection = pyqtSignal()

    def run(self):
        """
        Host: 8.8.8.8 (google-public-dns-a.google.com)
        OpenPort: 53/tcp
        Service: domain (DNS/TCP)
        """

        timeout = 3
        host = "8.8.8.8"
        port = 53
        connection_is_available = None

        while True:
            try:
                socket.setdefaulttimeout(timeout)
                socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))

                if connection_is_available == True:
                    continue

                self.spotted_connection.emit()
                connection_is_available = True

            except socket.error:
                if connection_is_available == False:
                    continue

                self.lost_connection.emit()
                connection_is_available = False


module_is_runned_directly = __name__ == "__main__"
if module_is_runned_directly:
    raise DirectRunError(
        "Database modules are not intended to run directly, they are produced for import usage only."
    )
