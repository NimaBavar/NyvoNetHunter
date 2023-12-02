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


from packages import (
    abstractproperty,
    extract_url,
    ip_address,
    QByteArray,
    cmd_input,
    requests,
    Literal,
    ABC,
)

__version__ = "5.13.9"
__author__ = "KhodeNima ( Nima Bavar )"
__built_date__ = "2023/11/13"


class DirectRunError(Exception):
    """Improper direct run of a module"""

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


class Connectable(ABC):
    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    @abstractproperty
    def endpoint(self) -> str:
        return self.__endpoint

    @endpoint.setter
    def endpoint(self, __endpoint):
        if not isinstance(__endpoint, str):
            endpoint_argument_type = type(__endpoint).__name__
            raise ValueError(
                f"Expected argument type passed for the parameter ( endpoint ): ( str ) | Not {endpoint_argument_type}"
            )

        self.__endpoint = __endpoint


class NyvoNetHunterIpAddress(Connectable):
    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    @property
    def endpoint(self) -> str:
        return self.__endpoint

    @endpoint.setter
    def endpoint(self, __endpoint):
        
        if not isinstance(__endpoint, str):
            endpoint_argument_type = type(__endpoint).__name__
            raise ValueError(f"Expected argument type passed for the parameter ( endpoint ): ( str ) | Not: {endpoint_argument_type}")
            
        if not is_valid_ip(__endpoint):
            raise TypeError("Invalid Ip address passed.")
    
        self.__endpoint = __endpoint
        

class NyvoNetHunterUrl(Connectable):
    def __init__(self, endpoint: str):
        self.endpoint = endpoint
        
    
    @property
    def endpoint(self) -> str:
        return self.__endpoint
        
    
    @endpoint.setter
    def endpoint(self, __endpoint) -> str:
    
        if not isinstance(__endpoint, str):
            endpoint_argument_type = type(__endpoint).__name__
            raise ValueError(f"Expected argument type passed for the parameter ( endpoint ): ( str ) | Not: {endpoint_argument_type}")
            
        if not is_valid_url(__endpoint):
            raise TypeError("Invalid url passed.")
            
        self.__endpoint = __endpoint

def find_endpoint_type(self, connectable: Connectable) -> Literal["ip", "url"]:
    """
    Returns:
        str: ( `ip` ), ( `url` )
    """
    
    if not isinstance(connectable, Connectable):
        connectable_argument_type = type(connectable).__name__
        raise ValueError(
            f"Expected argument type passed for the parameter ( connectable ): Connectable | Not: ( {connectable_argument_type} )"
        )
            
    if isinstance(str, Connectable):
        connectable_endpoint = connectable
            
    connectable_endpoint = connectable.endpoint
        
    endpoint_is_ip_address = is_valid_ip(connectable_endpoint)
    endpoint_is_url = is_valid_url(connectable_endpoint)
        
    if not endpoint_is_ip_address and not endpoint_is_url:
        raise TypeError("The connectable endpoint type is not communicatable")
            
    if endpoint_is_ip_address and endpoint_is_url:
        assert "Validation error"
            
    if endpoint_is_ip_address:
        return "ip"
            
    if endpoint_is_url:
        return "url"



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
        raise ValueError(
            f"Expected argument type passed for the parameter ( url ): (str) | Not: ( {url_argument_type} )"
        )
        
    url_contains_schema = url.startswith("https://") or url.startswith("http://")
    
    if not url_contains_schema:
        url = f"http://{url}"

    extracted_url_segments = extract_url(url).__dict__
    extracted_segments_list = [segment for segment in extracted_url_segments.values()]
    
    url_has_domain_name = bool(extracted_segments_list[1])
    url_has_top_level_domain = bool(extracted_segments_list[2])
    
    url_is_valid = all([url_has_domain_name, url_has_top_level_domain])
    
    if url_is_valid:
        return True
        
    return False
    
def make_api_call(connectable: Connectable) -> str:
    api_key = "mWNfs+SWsyZk+Wx6r5AyGw==cFD5QGOQyTJo3Xzb"
        
    connectable_endpoint = connectable.endpoint
    connectable_endpoint_type = find_endpoint_type(connectable_endpoint)
        
        
    api_key = QByteArray("X-Api-Key".encode())
    api_key_value = QByteArray(api_key.encode())

    api_key_header = {api_key: api_key_value}

    if not isinstance(connectable, str):
        connectable_argument_type = type(connectable).__name__
        raise ValueError(
            "Expected argument type passed for the parameter ( connectable ): Connectable | Not: ( Connectable ) |"
        )

    if connectable_endpoint_type:
         ...
        

def clean_terminal() -> None:
    cmd_input("cls")


module_is_runned_directly = __name__ == "__main__"

if module_is_runned_directly:
    clean_terminal()
    raise DirectRunError(
        "Database modules are not intended to run directly. They are produced for import usage only."
    )