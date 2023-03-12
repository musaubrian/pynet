"""Module defines a class PyshareGUI"""
import customtkinter
from app.GUI.file_picker import SelectFileWindow


class PyshareGUI(customtkinter.CTk):
    """
    Graphical Interface for the PyShare programme
    """

    def __init__(self) -> None:
        super().__init__()
        self.title("PyShare | File sharing")
        self.resizable(width=False, height=False)
        self.select_file_window = None
        self.button_style = customtkinter.CTkFont(size=26, family="Arial")

        # Setup PyShare logo(name)
        self.pyshare_logo = customtkinter.CTkLabel(
            master=self,
            text="PyShare",
            font=customtkinter.CTkFont(size=50, family="Arial"),
        )
        self.pyshare_logo.grid(
            column=0,
            columnspan=4,
            row=0,
            rowspan=2,
            sticky="ew",
            padx=20,
            pady=(20, 5)
        )
        # Description below the PyShare name
        self.pyshare_description = customtkinter.CTkLabel(
            master=self,
            text="File sharing made easy",
            font=customtkinter.CTkFont(size=20, family="Arial"),
        )
        self.pyshare_description.grid(
            column=0, columnspan=4, row=2, sticky="ew", padx=20, pady=5
        )

        # Buttons to launch client | server
        self.send_button = customtkinter.CTkButton(
            self, text="Send", command=self.open_file_popup, font=self.button_style
        )
        self.send_button.grid(row=3, column=0, columnspan=2, padx=30, pady=30)

        self.receive_button = customtkinter.CTkButton(
            self, text="Receive", font=self.button_style
        )
        self.receive_button.grid(row=3, column=2, columnspan=2, padx=30, pady=30)

    def open_file_popup(self):
        """
        Opens the file selector window
        """
        if (
            self.select_file_window is None
            or not self.select_file_window.winfo_exists()
        ):
            self.select_file_window = SelectFileWindow(self)
        else:
            self.select_file_window.focus()
