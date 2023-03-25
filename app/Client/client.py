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

    def strip_slashes(self, slashed_var: str) -> str:
        """Strips the slashes from the filename,
        which is sent as a file path"""
        self.slashed_var = slashed_var
        self.unclean_file_name = self.slashed_var.split("/") or self.slashed_var.split(
            "\\"
        )
        self.actual_name = self.unclean_file_name[-1]
        return self.actual_name

    def receive_file(self):
        while True:
            self.file_data = self.pyshare_client.recv(1024).decode()
            if not self.file_data:
                break
            elif self.file_data == "done":
                self.pyshare_client.close()
                break
            else:
                self.file_name, self.file_size = self.file_data.split()
                self.actual_file_name = self.strip_slashes(self.file_name)
                self.file_size = int(self.file_size)
                self.received_data = b""

                while len(self.received_data) < self.file_size:
                    self.data_chunk = self.pyshare_client.recv(1024)
                    self.received_data += self.data_chunk

                with open(self.actual_file_name, "wb") as f:
                    f.write(self.received_data)
