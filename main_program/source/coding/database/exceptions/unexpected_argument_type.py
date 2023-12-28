"""
The holder module for the UnexpectedArgumentTypeError exception class
"""


from inspect import isclass


class UnexpectedArgumentTypeError(ValueError):
    def __init__(self, inputted_argument, expected_argument_type: object) -> None:
        self.passed_argument = inputted_argument
        self.passed_argument_type = inputted_argument
        self.expected_argument_type = expected_argument_type

        self._generate_error_message()
        super().__init__(self.error_message)

    def _generate_error_message(self):
        self.error_message = (
            f"Expected argument type passed for the parameter \
( {self.passed_argument} ): ( {self.expected_argument_type} ) | Not ( {self.passed_argument_type} )."
            )
        
    @property
    def passed_argument_type(self):
        return self._passed_argument_type
    
    @passed_argument_type.setter
    def passed_argument_type(self, argument_type):
        self._passed_argument_type = type(argument_type).__name__

    @property
    def expected_argument_type(self):
        return self._expected_argument_type
    
    @expected_argument_type.setter
    def expected_argument_type(self, argument):
        if not isclass(argument):
            raise ValueError("The ( expected_argument_type ) argument must be object| e.x: ( str, tuple... )")
        
        self._expected_argument_type = argument.__name__