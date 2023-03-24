"""Receive file popup"""
import customtkinter


class RecieveFileWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Recieve file")
        self.resizable(width=False, height=False)

        self.text_label = customtkinter.CTkLabel(
            master=self,
            text="Enter pairing key: ",
            font=customtkinter.CTkFont(size=30, family="Arial"),
        )
        self.text_label.grid(
            row=0, column=0, columnspan=7, padx=30, pady=(30, 10), sticky="nsew"
        )
        self.pairing_key = customtkinter.CTkEntry(
            self,
            font=customtkinter.CTkFont(size=25, family="Arial"),
            height=40,
            placeholder_text="200-123-14-154",
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
            text="pair",
            font=customtkinter.CTkFont(size=24, family="Arial"),
            command=self.get_key,
        )
        self.pair.grid(row=4, column=0, columnspan=5, padx=30, pady=30, sticky="nsew")

        self.error_label = customtkinter.CTkLabel(
                self,
                text="Input is invalid, try again",
                fg_color="red",
                font=customtkinter.CTkFont(size=25, family="Arial"),
                )
        self.error_label.grid(
                row=3, column=0, columnspan=5, sticky="nsew", padx=30, pady=10
                )
        self.error_label.grid_remove()

    def get_key(self):
        """Get the key from the text box"""
        key_value = self.pairing_key.get()
        if len(key_value) != 9 and "-" not in key_value:
            self.error_label.grid()
        else:
            self.error_label.grid_remove()
            print(key_value)
