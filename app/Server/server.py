"""Module server is the entry point for class server."""
import socket
from typing import List


class PyshareServer:
    """Defines functions related to the pyshare server."""

    def __init__(self) -> None:
        self.socket = socket
        self.raw_ip = ""
        self.reversed_ip: List[str] = []
        self.gen_key: str = ""
        self.port = 9999

    def _get_ip(self) -> str:
        """Returns hosts ip address."""
        self._raw_ip = self.socket.gethostbyname(self.socket.gethostname())
        return self._raw_ip

    def create_pairing_key(self) -> str:
        """Returns the reversed ip as a key to connect to."""
        self.raw_ip = self._get_ip()
        self.reversed_ip = self.raw_ip.split(".")[::-1]
        self.gen_key: str = "-".join(self.reversed_ip)

        return self.gen_key

    def create_service(self):
        """Listens for connection to server."""
        self._pyshare_server = self.socket.socket(
            self.socket.AF_INET, self.socket.SOCK_STREAM
        )
        self._pyshare_server.bind((self.raw_ip, self.port))
        self._pyshare_server.listen()
        print(f"waiting for connection on {self.raw_ip}:{self.port}")
        self._pyshare_client, self.address = self._pyshare_server.accept()

    def send_files(self, files_to_send: List[str]):
        """Send the files over the network.

        Args::
            files_to_send(List[str]): list of the file names/path
            to convert to bytes and send
        """

        for file in files_to_send:
            with open(file, "rb") as f:
                self._file_data = f.read()

            self._pyshare_client.sendall(f"{file} {len(self._file_data)}".encode())
            self._chunk_size = 1024
            self._num_chunks = len(self._file_data) // self._chunk_size
            self._remainder = len(self._file_data) % self._chunk_size

            for i in range(self._num_chunks):
                self._start = i * self._chunk_size
                self._end = (i + 1) * self._chunk_size

            self._chunk = self._file_data[self._start : self._end]
            self._pyshare_client.sendall(self._chunk)
            if self._remainder:
                self._pyshare_client.sendall(self._file_data[-self._remainder :])

        self._pyshare_client.sendall(b"done")
        self._pyshare_client.close()
        self._pyshare_server.close()
