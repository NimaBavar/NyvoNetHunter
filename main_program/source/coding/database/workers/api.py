"""
# The storage module for the back-end API of the project.
"""


def setup_database_import_path() -> None:
    from sys import path as module_paths
    import pathlib

    project_root_directory = pathlib.Path.cwd()

    module_paths.append(f"{project_root_directory}/main_program/source/coding/database")
    module_paths.append(f"{project_root_directory}/main_program/source/coding")


setup_database_import_path()

from packages import (
    ConnectionError,
    abstractmethod,
    extract_url,
    ip_address,
    pyqtSignal,
    cmd_input,
    platform,
    requests,
    Literal,
    QThread,
    QObject,
    folium,
    loads,
    sleep,
    Dict,
    ABC,
    re,
)
from exceptions.direct_run_error import DirectRunError


class Connectable(ABC):
    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    @property
    @abstractmethod
    def endpoint(self) -> str:
        return self._endpoint

    @endpoint.setter
    def endpoint(self, _endpoint):
        if not isinstance(_endpoint, str):
            endpoint_argument_type = type(_endpoint).__name__
            raise ValueError(
                f"Expected argument type passed for the parameter ( endpoint ): ( str ) | Not {endpoint_argument_type}"
            )

        self._endpoint = _endpoint
        

class NyvoNetHunterRequestManager(QObject):
    request_started = pyqtSignal()
    request_sent = pyqtSignal()

    failed_to_send = pyqtSignal()

    received_valid_response = pyqtSignal()
    received_invalid_response = pyqtSignal()


    available_http_methods = ["get", "post", "put", "delete"]
    def __init__(
        self,
        url: str,
        data: Dict,
        headers: Dict,
        method: Literal["get", "post", "put", "delete"],
    ):
        self.url = url
        self.data = data
        self.headers = headers
        self.method = method

        super(QObject, self).__init__()

    def fire(self) -> requests.Response:
        self.request_started.emit()


        try:
            self.response = requests.request(method=self.method, url=self.url, data=self.data, headers=self.headers, timeout=20)
            self.request_sent.emit()

        except Exception as e:
            self.failed_to_send.emit()
            return self.response


    def check_response_is_valid(self) -> bool | pyqtSignal:
        if self.response.ok:
            self.received_valid_response.emit()
            return True

        self.received_invalid_response.emit()
        return False


    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, _url):
        if not isinstance(_url, str):
            url_argument_type = type(_url).__name__
            raise ValueError(
                f"Expected argument type passed for the parameter( url ): ( str ) | Not ( {url_argument_type}."
            )

        url_is_invalid = not is_valid_url(_url)
        if url_is_invalid:
            raise TypeError("That is not a valid url.")

        self._url = _url

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, _data):
        if not isinstance(_data, dict):
            data_argument_type = type(_data).__name__
            raise ValueError(
                f"Expected argument type passed for the parameter ( data ): ( dict ) | Not: ( {data_argument_type} )"
            )

        self._data = _data

    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, _headers):
        if not isinstance(_headers, dict):
            headers_argument_type = type(_headers).__name__
            raise ValueError(
                f"Expected argument type passed for the parameter ( headers ): ( dict ) | Not: ( {headers_argument_type} )"
            )

        self._headers = _headers

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, _method):

        if not isinstance(_method, str):
            method_argument_type = type(_method).__name__
            raise ValueError(
                f"Expected argument types passed for the parameter ( method ): ( str ) | Not: {method_argument_type}"
            )

        if not _method in self.available_http_methods:
            raise TypeError("That is not a valid http method.")

        self._method = _method


class NyvoNetHunterIpAddress(Connectable):
    def __init__(self, ip_address: str):
        self.endpoint = ip_address

    def remove_paths(self) -> str:
        """
        Removes web paths from a URL.

        Parameters
        ----------
        url | str
            The web Univeral Resource Locator.

        Returns
        -------
        str
            The url with the removed paths.
        """

        url = self.endpoint

        url_has_suffix = url.startswith("http://") or url.startswith("https://")
        if url_has_suffix:

            if url.startswith("https://"):
                mutated_url = url[len("https://"):]

            if url.startswith("http://"):
                mutated_url = url[len("http://"):]

        if not url_has_suffix:
            mutated_url = url

        path_removal_pattern = r"/\S*"
        formatted_url = re.sub(pattern=path_removal_pattern, repl="", string=mutated_url)

        if url_has_suffix:
            formatted_url = f"http://{formatted_url}"
        
        return formatted_url

    @property
    def endpoint(self) -> str:
        return self._ip_address

    @endpoint.setter
    def endpoint(self, _ip_address):
        if not isinstance(_ip_address, str):
            endpoint_argument_type = type(_ip_address).__name__
            raise ValueError(
                f"Expected argument type passed for the parameter ( endpoint ): ( str ) | Not: {endpoint_argument_type}"
            )

        if not is_valid_ip(_ip_address):
            raise TypeError("Invalid Ip address passed.")

        self._ip_address = _ip_address


class NyvoNetHunterUrl(Connectable):
    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    def remove_paths(self, apply_to_endpoint: bool=False) -> str:
        """
        Removes web paths from a URL.

        Parameters
        ----------
        url | str
            The web Univeral Resource Locator.

        Returns
        -------
        bool, default=False
            Wether to apply the result on the endpoint.
        """

        url_has_suffix = False
        url_has_secure_suffix = False

        url = self.endpoint

        if url.startswith("https://"):
            url_has_suffix = True
            url_has_secure_suffix = True

            mutated_url = url[len("https://"):]

        if url.startswith("http://"):
            url_has_suffix = True
            mutated_url = url[len("http://"):]

        if not url_has_suffix:
            mutated_url = url

        path_removal_pattern = r"/\S*"
        formatted_url = re.sub(pattern=path_removal_pattern, repl="", string=mutated_url)

        if url_has_secure_suffix:
            formatted_url = f"https://{formatted_url}"

        if url_has_suffix and not url_has_secure_suffix:
            formatted_url = f"http://{formatted_url}"
            return formatted_url
    
        if apply_to_endpoint:
            self.endpoint = formatted_url

        return formatted_url

    def remove_suffix(self, apply_to_endpoint=False) -> str:
        url_suffix_pattern = r"https?://"
        mutated_url = re.sub(pattern=url_suffix_pattern, repl="", string=self.endpoint)

        if apply_to_endpoint:
            self.endpoint = mutated_url

        return mutated_url

    @property
    def endpoint(self) -> str:
        return self._endpoint

    @endpoint.setter
    def endpoint(self, _endpoint: str) -> None:
        if not isinstance(_endpoint, str):
            endpoint_argument_type = type(_endpoint).__name__
            raise ValueError(
                f"Expected argument type passed for the parameter ( endpoint ): ( str ) | Not: {endpoint_argument_type}"
            )

        if not is_valid_url(_endpoint):
            raise TypeError("Invalid url passed.")
        
        self._endpoint = _endpoint


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


def find_endpoint_type(connectable: Connectable | str) -> Literal["ip", "str"]:
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
        raise TypeError("Invalid IP or URL.")

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

    url_contains_scheme = url.startswith("https://") or url.startswith("http://")
    if not url_contains_scheme:
        url = f"http://{url}"

    
    extracted_url_segments = extract_url(url=url)._asdict()

    url_has_domain = bool(extracted_url_segments["domain"])
    url_has_top_domain = bool(extracted_url_segments["suffix"])
    url_is_valid = all([url_has_top_domain, url_has_domain])
    
    return url_is_valid



def clean_terminal() -> None:
    runner_operating_system = platform(terse=True)
    operating_system_is_windows = runner_operating_system.lower().startswith("windows")
    operating_system_is_linux = runner_operating_system.lower().startswith("linux")

    if operating_system_is_windows:
        cmd_input("cls")
        return

    if operating_system_is_linux:
        cmd_input("clear")


def simplify_text(text: str) -> str:
    """Simplifies a long text for previews.

    ex: MyNameIsAlex -> MyName...
    """

    if not isinstance(text, str):
        argument_type = type(str).__name__
        raise ValueError(f"Expected argument type passed for the parameter ( text ): ( str ) | Not: ( {argument_type} )")


    text_lenght = len(text)
    if not text_lenght >= 6:
        return text
    
    simplified_string = f"{text[0:6]}..."
    return simplified_string


module_is_runned_directly = __name__ == "__main__"
if module_is_runned_directly:
    raise DirectRunError(
        "Database modules are not intended to run directly, they are produced for import usage only."
    )
