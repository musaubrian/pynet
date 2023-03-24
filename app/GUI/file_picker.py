"""Module defines class SelectFileWindow"""
from typing import List
import customtkinter
import app.GUI.picked_files as picked_files
from app.Server.server import PyshareServer


class SelectFileWindow(customtkinter.CTkToplevel):
    """
    Opens New window to select files or directories.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_path = None
        self.title("PyShare | select files")
        self.resizable(width=False, height=False)
        self.button_style = customtkinter.CTkFont(size=24, family="Arial")
        self.file_paths: List[str] = []
        self.dir_path = ""

        self.server = PyshareServer()
        self.pairing_key: str = self.server.create_pairing_key()

        self.picker_label = customtkinter.CTkLabel(
            master=self,
            text="Pick a file or a folder to transfer",
            font=customtkinter.CTkFont(size=30, family="Arial"),
        )
        self.picker_label.grid(
            row=0,
            rowspan=2,
            column=0,
            columnspan=4,
            padx=20,
            pady=(20, 10),
            sticky="nsew",
        )

        self.pairing_key_label = customtkinter.CTkLabel(
            master=self,
            text=f"Pairing key: {self.pairing_key}",
            font=self.button_style,
            fg_color="blue",
        )
        self.pairing_key_label.grid(column=0, columnspan=5, row=2)
        self.line = customtkinter.CTkLabel(master=self, text="- " * 55)
        self.line.grid(column=0, columnspan=4, row=3)

        self.list_file = picked_files.PickedFilesFrame(self, self.file_paths)
        self.list_file.grid(column=0, columnspan=4, padx=10, pady=10)

        self.pick_file_btn = customtkinter.CTkButton(
            master=self,
            text="Pick files",
            command=self.open_file_dialog,
            font=self.button_style,
        )
        self.pick_file_btn.grid(
            column=0, columnspan=5, row=5, padx=30, pady=30, sticky="ew"
        )

        self.start_transfer = customtkinter.CTkButton(
            master=self,
            text="Transfer",
            font=customtkinter.CTkFont(size=30, family="Arial", weight="bold"),
            command=self.handle_transfer,
        )
        self.start_transfer.grid(
            column=1, columnspan=2, row=6, sticky="ew", pady=(10, 30)
        )

        self.list_file = picked_files.PickedFilesFrame(self, self.file_paths, width=400)
        self.list_file.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

    def open_file_dialog(self) -> None:
        """
        Opens the file picker pop up
        gets the path to the file
        """
        self.file_path = customtkinter.filedialog.askopenfile()
        if self.file_path is not None:
            if self.file_path.name not in self.file_paths:
                self.file_paths.append(self.file_path.name)
                print(self.file_paths)
                self.list_file.display_files(self.file_paths)
        else:
            print("File already selected")

    def open_dir_dialog(self) -> None:
        """ """
        self.dir_path = customtkinter.filedialog.askdirectory()
        print(f"Selected path: {self.dir_path}")

    def handle_transfer(self) -> None:
        """Handles the transfer logic"""
        print("Transfer button clicked")
