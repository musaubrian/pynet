"""module server is the entry point for class server"""
import socket
from typing import List


class PyshareServer:
    """Defines functions related to the pyshare server"""

    def __init__(self) -> None:
        self.socket = socket
        self.raw_ip = ""
        self.reversed_ip: List[str] = []
        self.gen_key: str = ""
        self.port = 9999

    def _get_ip(self) -> str:
        """Returns hosts ip address
        (*private method)
        """
        self._raw_ip = self.socket.gethostbyname(self.socket.gethostname())
        return self._raw_ip

    def create_pairing_key(self) -> str:
        """Returns the reversed ip as a key to connect to"""
        self.raw_ip = self._get_ip()
        self.reversed_ip = self.raw_ip.split(".")[::-1]
        self.gen_key: str = "-".join(self.reversed_ip)

        return self.gen_key

    def create_service(self):
        """Listens for connection to server"""
        self.pyshare_server = self.socket.socket(
            self.socket.AF_INET, self.socket.SOCK_STREAM
        )
        self.pyshare_server.bind((self.raw_ip, self.port))
        self.pyshare_server.listen()
        print(f"waiting for connection on {self.raw_ip}:{self.port}")
        self.pyshare_client, self.address = self.pyshare_server.accept()
