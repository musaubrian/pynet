"""Module defines a class PyshareGUI"""
import customtkinter
from app.GUI.file_picker import SelectFileWindow


class PyshareGUI(customtkinter.CTk):
    """
    Graphical Interface for the PyShare programme
    """

    def __init__(self) -> None:
        super().__init__()
        self.title("PyShare")
        self.geometry("500x400")
        self.minsize(width=250, height=200)
        self.resizable(width=True, height=True)
        self.select_file_window = None
        self.button_style = customtkinter.CTkFont(size=24, family="Arial")

        self.pyshare_logo = customtkinter.CTkLabel(
            master=self,
            text="PyShare",
            font=customtkinter.CTkFont(size=40, family="Arial"),
        )
        self.pyshare_logo.grid(column=0, columnspan=3, row=0, sticky="ew")

        self.send_button = customtkinter.CTkButton(
            self, text="Send", command=self.open_file_popup, font=self.button_style
        )
        self.send_button.grid(row=1, column=1, columnspan=2, padx=30, pady=30)

        self.receive_button = customtkinter.CTkButton(
            self, text="Receive", font=self.button_style
        )
        self.receive_button.grid(row=1, column=3, columnspan=2, padx=30, pady=30)

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
