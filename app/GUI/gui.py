"""Module defines a class PyshareGUI."""
import customtkinter

from app.GUI.file_picker import SelectFileWindow
from app.GUI.receive_file import RecieveFileWindow


class PyshareGUI(customtkinter.CTk):
    """Graphical Interface for the PyShare program."""

    def __init__(self) -> None:
        super().__init__()
        self.title("PyShare | File sharing")
        self.resizable(width=False, height=False)
        self.select_file_window = None

        # Setup PyShare logo(name)
        self.pyshare_logo = customtkinter.CTkLabel(
            master=self,
            text="PyShare",
            font=self.set_font_style(font_size=50, font_weight="bold")
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
            font=self.set_font_style(font_size=20, font_weight="")
            )
        self.pyshare_description.grid(
            column=0, columnspan=4, row=2, sticky="ew", padx=20, pady=5
        )

        # Buttons to launch client | server
        self.send_button = customtkinter.CTkButton(
            self,
            text="Send",
            command=self.open_send_popup,
            font=self.set_font_style(font_size=26, font_weight="")
        )
        self.send_button.grid(
                row=3, column=0, columnspan=2, padx=30, pady=30)

        self.receive_button = customtkinter.CTkButton(
            self,
            text="Receive",
            font=self.set_font_style(font_size=26, font_weight=""),
            command=self.open_recieve_popup,
        )
        self.receive_button.grid(
                row=3, column=2, columnspan=2, padx=30, pady=30)

    def set_font_style(
            self, font_size: int, font_weight: str
            ) -> customtkinter.CTkFont:
        """Return CTkFont styles for the button or label"""
        if font_weight == "bold":
            return customtkinter.CTkFont(
                    size=font_size, weight="bold", family="Arial")

        return customtkinter.CTkFont(size=font_size, family="Arial")

    def open_send_popup(self):
        """Open the file selector window."""
        if (
            self.select_file_window is None
            or not self.select_file_window.winfo_exists()
        ):
            self.select_file_window = SelectFileWindow(self)
            self.iconify()
        else:
            self.select_file_window.focus()

    def open_recieve_popup(self):
        """Open the receive popup window."""
        if (
            self.select_file_window is None
            or not self.select_file_window.winfo_exists()
        ):
            self.select_file_window = RecieveFileWindow(self)
        else:
            self.select_file_window.focus()
