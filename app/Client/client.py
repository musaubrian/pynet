"""module contains contains a class PyshareClient
which is the entry point of the client operations"""
import socket


class PyshareClient:
    """contains client operations code"""

    def __init__(self, pairing_key: str) -> None:
        self.socket = socket
        self.pairing_key = pairing_key
        self.port: int = 9999

    def _get_client_ip(self) -> str:
        """gets the clients ip address"""
        self._client_ip = self.socket.gethostbyname(self.socket.gethostname())
        return self._client_ip

    def _tweak_ip(self) -> str:
        """return the servers raw ip"""
        self._unformatted_ip = self.pairing_key.split("-")[::-1]
        self._server_ip = ".".join(self._unformatted_ip)
        return self._server_ip

    def connect_to_service(self):
        """Creates a connection to the server"""
        self.server_ip = self._tweak_ip()
        self.pyshare_client = self.socket.socket(
            self.socket.AF_INET, self.socket.SOCK_STREAM
        )
        self.pyshare_client.connect((self.server_ip, self.port))
