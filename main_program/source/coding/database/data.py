"""
# The base data file of the project
---
"""


from packages import (
    cmd_input, 
    ip_address, 
    requests,
)

__version__ = "4.12.8"
__author__ = "KhodeNima ( Nima Bavar )"
__built_date__ = "2023/11/13"


class DirectRunError(Exception):
    """Improper direct run of a module
    """
    def __init__(self, error_message: str):
        self.error_message = error_message

    @property
    def error_message(self) -> str:
        return self.__error_message

    @error_message.setter
    def error_message(self, message) -> str:
        message_is_string = isinstance(message, str)
        message_is_not_valid = not message_is_string

        if message_is_not_valid:
            message_argument_type = type(message).__name__
            raise ValueError(
                f"Expected argument type passed for the parameter ( error_message ): ( str ) | Not: ( {message_argument_type} )"
            )

        self.__error_message = message
    
        
def is_valid_ip(ip: str) -> bool:

    if not isinstance(ip, str):
        ip_argument_type = type(ip).__name__
        raise ValueError(
            f"Expected argument type passed for the parameter ( ip ): ( str ) | Not: ( {ip_argument_type} )"
        )

    try:
        ip_address(ip)
        return True

    except ValueError:
        return False


def is_valid_ipv4(ip: str) -> bool:
    if not isinstance(ip, str):
        ip_argument_type = type(ip).__name__
        raise ValueError(
            f"Expected argument type passed for the parameter ( ip ): ( str ) | Not: ( {ip_argument_type} )"
        )

    if not is_valid_ip(ip):
        return False

    ip_version = ip_address(ip).version
    ip_version_is_ipv4 = ip_version == 4

    if ip_version_is_ipv4:
        return True

    return False


def is_valid_ipv6(ip: str):
    if not isinstance(ip, str):
        ip_argument_type = type(ip).__name__
        raise ValueError(
            f"Expected argument type passed for the parameter ( ip ): ( str ) | Not: ( {ip_argument_type} )"
        )

    if not is_valid_ip(ip):
        return False

    ip_version = ip_address(ip).version
    ip_version_is_ipv6 = ip_version == 6

    if ip_version_is_ipv6:
        return True

    return False
    

def is_valid_url(url: str) -> bool:

    if not isinstance(url, str):
        url_argument_type = type(url).__name__
        raise ValueError(f"Expected argument type passed for the parameter ( url ): (str) | Not: ( {url_argument_type} )")
        
    tries_count = 1
    
    for number in range(0, 3):
        try:
            response = requests.get(url=url)
            return True
            
        except:
            if tries_count == 2:
                return False
            
            url = f"https://{url}" 
            tries_count += 1
    
    
def clean_terminal() -> None:
    cmd_input("cls")


module_is_runned_directly = __name__ == "__main__"

if module_is_runned_directly:
    clean_terminal()
    raise DirectRunError(
        "Database modules are not intended to run directly. They are produced for import usage only."
    )