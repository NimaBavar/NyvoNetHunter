
"""
# The module for NyvoNetHunterPortScanner suite NoRunningSessionError Exception.
"""


class NoRunningSession(Exception):
    def __init__(self, error_message: str):
        """
        Use when an operation requires a running session to operate, but none is found.

        Parameters
        ----------
        error_message | str
            The error message to raise
        """
        self.error_message = error_message

    @property
    def error_message(self) -> str:
        return self._error_message

    @error_message.setter
    def error_message(self, message: str) -> None:
        if not isinstance(message, str):
            passed_argument_type = type(message).__name__
            raise ValueError(f"Expected argument type passed for the parameter ( error_message ): ( str ) | Not: ( {passed_argument_type} )")

        self._error_message = message
