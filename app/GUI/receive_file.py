"""Module defines a receive file popup."""
import customtkinter

from app.Client.client import PyshareClient


class RecieveFileWindow(customtkinter.CTkToplevel):
    """Create a top level window for the receive functionality."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Recieve file")
        self.resizable(width=False, height=False)
        self.pyshare_client = PyshareClient()

        self.text_label = customtkinter.CTkLabel(
            master=self,
            text="Enter pairing key: ",
            font=customtkinter.CTkFont(size=30, family="Arial"),
        )
        self.text_label.grid(
            row=0,
            column=0,
            columnspan=7,
            padx=30,
            pady=(30, 10),
            sticky="nsew"
        )
        self.pairing_key = customtkinter.CTkEntry(
            self,
            font=customtkinter.CTkFont(size=25, family="Arial"),
            height=40,
            placeholder_text="25-10-168-192",
        )
        self.pairing_key.grid(
            row=1,
            column=0,
            columnspan=7,
            padx=30,
            pady=10,
            sticky="nsew",
        )
        self.pair = customtkinter.CTkButton(
            master=self,
            text="Connect",
            font=customtkinter.CTkFont(size=24, family="Arial"),
            command=self.get_key,
        )
        self.pair.grid(
                row=7,
                column=0,
                columnspan=8,
                padx=30,
                pady=30,
                sticky="nsew"
                )

        self.sending = customtkinter.CTkLabel(
            master=self,
            text="Recieving...",
            font=customtkinter.CTkFont(size=24, family="Arial"),
        )
        self.sending.grid(
            row=6, column=0, columnspan=7, padx=30, pady=10, sticky="nsew"
        )
        self.sending.grid_remove()

        self.error_label = customtkinter.CTkLabel(
            self,
            text="Key is invalid, try again",
            fg_color="red",
            font=customtkinter.CTkFont(size=25, family="Arial"),
        )
        self.error_label.grid(
            row=3, column=0, columnspan=5, sticky="nsew", padx=30, pady=10
        )
        self.error_label.grid_remove()
        self.success_message = customtkinter.CTkLabel(
            self,
            text="Files saved at /Desktop/pyshare_received",
            font=customtkinter.CTkFont(size=20, family="Arial"),
        )
        self.success_message.grid(
            row=5, column=0, columnspan=5, sticky="nsew", padx=30, pady=10
        )
        self.success_message.grid_remove()

    def get_key(self):
        """Get the key from the text box."""
        key_value = self.pairing_key.get()
        if "-" not in key_value or\
                ((len(key_value) < 8 or len(key_value) > 15)):
                    self.error_label.grid()
        else:
            self.error_label.grid_remove()
            self.received = self.pyshare_client.receive_files(key_value)
            self.sending.grid()
            if self.received:
                self.sending.grid_remove()
                self.success_message.grid()
