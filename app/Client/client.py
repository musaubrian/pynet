"""Module contains a class PynetClient."""

import os
from pathlib import Path
import socket


class PynetClient:
    """Contain pynet client operations code."""

    def __init__(self) -> None:
        self.socket = socket
        self.port: int = 8080
        self.receiving = True

    def _get_client_ip(self) -> str:
        """Get the clients ip address."""
        self._client_ip = self.socket.gethostbyname(
                self.socket.gethostname())
        return self._client_ip

    def _tweak_ip(self, unformatted_ip: str) -> str:
        """Return the servers raw ip."""
        self._unformatted_ip = unformatted_ip.split("-")[::-1]
        self._server_ip = ".".join(self._unformatted_ip)
        return self._server_ip

    def connect_to_service(self, pairing_key: str):
        """Create a connection to the server."""
        self.server_ip = self._tweak_ip(pairing_key)
        self.pynet_client = self.socket.socket(
            self.socket.AF_INET, self.socket.SOCK_STREAM
        )
        print(self._server_ip)
        self.pynet_client.connect((self.server_ip, self.port))

    def _strip_slashes(self, slashed_var: str) -> str:
        """Strip the slashes from the filename."""
        self.slashed_var = slashed_var
        self.unclean_file_name = self.slashed_var.split("/")\
            or self.slashed_var.split("\\")
        self.actual_name = self.unclean_file_name[-1]
        return self.actual_name

    def receive_files(self, pairing_key: str):
        """Receive transfered data and writes to appropriate file name."""
        self.connect_to_service(pairing_key)
        while self.receiving:
            self.file_data = self.pynet_client.recv(1024).decode()
            if not self.file_data:
                break
            else:
                self.file_name, self.file_size = self.file_data.split()
                print(self.file_data)
                self.actual_file_name = self._strip_slashes(self.file_name)
                self.file_size = int(self.file_size)
                self.received_data = b""

                self.home_path = Path.home()
                self.full_path = Path(
                    os.path.join(
                        self.home_path,
                        "Desktop",
                        "pynet_received",
                        self.actual_file_name,
                    )
                )

                while len(self.received_data) < self.file_size:
                    self.data_chunk = self.pynet_client.recv(5120)
                    self.received_data += self.data_chunk

                with open(self.full_path, "wb") as f:
                    f.write(self.received_data)
            self.receiving = False
