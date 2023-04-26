"""Module server is the entry point for class server."""
import socket
from typing import List

import netifaces


class PynetServer:
    """Define functions related to the pynet server."""

    def __init__(self) -> None:
        self.socket = socket
        self.raw_ip = ""
        self.reversed_ip: List[str] = []
        self.interfaces = netifaces.interfaces()
        self.gen_key: str = ""
        self.port: int = 8080

    def _get_ip(self) -> str:
        """Return hosts ip address."""
        for interface in self.interfaces:
            interface_details = netifaces.ifaddresses(interface)
            if netifaces.AF_INET in interface_details:
                addresses = interface_details[netifaces.AF_INET]
                if len(addresses) > 0 and 'addr' in addresses[0]\
                        and not addresses[0]['addr'].startswith('127.'):
                    self._raw_ip = addresses[0]['addr']
                    break
        return self._raw_ip

    def create_pairing_key(self) -> str:
        """Return the reversed ip as a key to connect to."""
        self.raw_ip = self._get_ip()
        self.reversed_ip = self.raw_ip.split(".")[::-1]
        self.gen_key: str = "-".join(self.reversed_ip)

        return self.gen_key

    def create_service(self):
        """Listen for connection to server."""
        self._pynet_server = self.socket.socket(
            self.socket.AF_INET, self.socket.SOCK_STREAM
        )
        self._pynet_server.bind((self.raw_ip, self.port))
        self._pynet_server.listen()
        print(f"waiting for connection on {self.raw_ip}:{self.port}")
        self._pynet_client, self.address = self._pynet_server.accept()
        print(f"connected to {self.address}")

    def replace_spaces(self, file: str) -> str:
        """Replace spaces with underscores.

        ---
        >>> from app.Server.server import PynetServer
        >>> server.replace_spaces("file name with spaces.mp4")
        'file_name_with_spaces.mp4'
        """
        self.clean_filename = file.replace(" ", "_")
        return self.clean_filename

    def send_files(self, files_to_send: List[str]):
        """Send the files over the network.

        Args::
            files_to_send(List[str]): list of the file names/path
                to convert to bytes and send.
        """
        for file in files_to_send:
            with open(file, "rb") as f:
                self._file_data = f.read()

            self.file_name = self.replace_spaces(file)

            self._pynet_client.sendall(
                    f"{self.file_name} {len(self._file_data)}".encode())
            self._chunk_size = 5120
            self._num_chunks = len(self._file_data) // self._chunk_size
            self._remainder = len(self._file_data) % self._chunk_size

            for i in range(self._num_chunks):
                self._start = i * self._chunk_size
                self._end = (i + 1) * self._chunk_size
                self._chunk = self._file_data[self._start:self._end]
                self._pynet_client.sendall(self._chunk)

            if self._remainder:
                self._pynet_client.sendall(
                        self._file_data[-self._remainder:])

            print(f"Sent {self.file_name} successfully")

        self._pynet_client.sendall(b" ")
        self._pynet_client.close()
        self._pynet_server.close()
