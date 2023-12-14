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
    QThread,
    ABC,
)

__version__ = "5.18.20"
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
            error_message_argument_type = type(message).__name__
            raise ValueError(
                f"Expected argument type passed for the parameter ( error_message ): ( str ) | Not: ( {error_message_argument_type} )"
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
    def __init__(self, ip_address: str):
        self.endpoint = ip_address

    @property
    def endpoint(self) -> str:
        return self.__ip_address

    @endpoint.setter
    def endpoint(self, __ip_address):
        if not isinstance(__ip_address, str):
            endpoint_argument_type = type(__ip_address).__name__
            raise ValueError(
                f"Expected argument type passed for the parameter ( endpoint ): ( str ) | Not: {endpoint_argument_type}"
            )

        if not is_valid_ip(__ip_address):
            raise TypeError("Invalid Ip address passed.")

        self.__ip_address = __ip_address


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
            raise ValueError(
                f"Expected argument type passed for the parameter ( endpoint ): ( str ) | Not: {endpoint_argument_type}"
            )

        if not is_valid_url(__endpoint):
            raise TypeError("Invalid url passed.")

        self.__endpoint = __endpoint


def generate_valid_connectable(endpoint: str) -> Connectable:
    if not isinstance(endpoint, str):
        endpoint_argument_type = type(endpoint).__name__
        raise ValueError(
            f"Expected argument type passed for the parameter ( endpoint ): str | Not: {endpoint_argument_type}"
        )

    endpoint_type = find_endpoint_type(endpoint)

    try:
        if endpoint_type == "ip":
            generated_connectable = NyvoNetHunterIpAddress(endpoint)

        if endpoint_type == "url":
            generated_connectable = NyvoNetHunterUrl(endpoint)
            

    except ValueError:
        raise ValueError("Invalid ip or URL.")

    return generated_connectable


def find_endpoint_type(connectable: [Connectable, str]) -> Literal["ip", "url"]:
    """
    Returns:
        str: ( `ip` ), ( `url` )
    """

    if not isinstance(connectable, (Connectable, str)):
        connectable_argument_type = type(connectable).__name__
        raise ValueError(
            f"Expected argument types passed for the parameter ( connectable, str ): Connectable | Not: ( {connectable_argument_type} )"
        )

    if isinstance(connectable, str):
        connectable_endpoint = connectable

    else:
        connectable_endpoint = connectable.endpoint

    
    endpoint_is_ip_address = is_valid_ip(connectable_endpoint)
    endpoint_is_url = is_valid_url(connectable_endpoint)

    if not endpoint_is_ip_address and not endpoint_is_url:
        raise TypeError("Invalid IP or URL")

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


def examine_endpoint(connectable: Connectable) -> str:
    api_key = "KBvhRDGVffUsQQ97m1Cm6SkmBERj8NLXPqZH8A0y"
    ip_lookup_api_url = "https://api.api-ninjas.com/v1/iplookup?address="
    url_lookup_api_url = "https://api.api-ninjas.com/v1/urllookup?url="

    if not isinstance(connectable, Connectable):
        connectable_argument_type = type(connectable).__name__
        raise ValueError(
            f"Expected argument type passed for the parameter ( connectable ): Connectable | Not: ( {connectable_argument_type} )"
        )

    try:
        connectable_endpoint_type = find_endpoint_type(connectable=connectable)

    except (TypeError, ValueError) as exception:
        error_type = type(exception)
        error_message = repr(exception)

        raise error_type(error_message)

    api_key_sign = "X-Api-Key"
    api_key_value = api_key
    api_key_header = {api_key_sign: api_key_value}

    if connectable_endpoint_type == "ip":
        response = requests.get(
            f"{ip_lookup_api_url}{connectable.endpoint}", headers=api_key_header
        )

    if connectable_endpoint_type == "url":
        response = requests.get(
            f"{url_lookup_api_url}{connectable.endpoint}", headers=api_key_header
        )

    if response.ok:
        return response.text


def clean_terminal() -> None:
    cmd_input("cls")


module_is_runned_directly = __name__ == "__main__"

if module_is_runned_directly:
    clean_terminal()
    raise DirectRunError(
        "Database modules are not intended to run directly. They are produced for import usage only."
    )
