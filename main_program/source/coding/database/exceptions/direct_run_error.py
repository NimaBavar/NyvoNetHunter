"""
# The storage module for the direct run errro exception.
"""


class DirectRunError(Exception):
    """Improper direct run of a module"""

    def __init__(self, error_message: str):
        self.error_message = error_message

    @property
    def error_message(self) -> str:
        return self._error_message

    @error_message.setter
    def error_message(self, message) -> str:
        message_is_string = isinstance(message, str)
        message_is_not_valid = not message_is_string

        if message_is_not_valid:
            error_message_argument_type = type(message).__name__
            raise ValueError(
                f"Expected argument type passed for the parameter ( error_message ): ( str ) | Not: ( {error_message_argument_type} )"
            )

        self._error_message = message


module_is_runned_directly = __name__ == "__main__"
if module_is_runned_directly:
    raise DirectRunError("Database modules are not intended to run directly, they are produced for import usage only.")
