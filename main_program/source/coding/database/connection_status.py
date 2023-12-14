"""
# The parrallelar daemon thread for testing the user's internet access
"""


from packages import Thread, ThreadError
from packages import requests


def is_connection_available() -> None:
    while True:
        try:
            requests.get("https://google.com")
            return True

        except requests.exceptions.ConnectionError:
            return False


def setup_connection_status_thread() -> Thread:
    t_1 = Thread(target=is_connection_available, daemon=True)
    return t_1