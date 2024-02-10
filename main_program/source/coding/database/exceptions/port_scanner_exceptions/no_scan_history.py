"""
The module for NyvoNetHunterTcpScanner suite NoScanHistoryError exception.
"""


class NoScanHistoryError(Exception):
    def __init__(self, error_message: str="No scan found.") -> None:
        super().__init__(error_message)

    @property
    def error_message(self) -> str:
        return self._error_message

    @error_message.setter
    def error_message(self, message: str) -> None:
        if not isinstance(message, str):
            argument_type = type(message).__name__
            raise ValueError(f"Expected argument type passed for the parameter ( error_message ): ( str ) | Not: ( {argument_type} )")


        self._error_message = message
