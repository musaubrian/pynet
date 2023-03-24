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
