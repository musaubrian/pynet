"""Module defines class SelectFileWindow"""
import customtkinter


class SelectFileWindow(customtkinter.CTkToplevel):
    """
    Opens New window to select files or directories.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("PyShare | select files")
        self.button_style = customtkinter.CTkFont(size=24, family="Arial")

        self.picker_label = customtkinter.CTkLabel(
            master=self,
            text="Pick a file or a folder to transfer",
            font=customtkinter.CTkFont(size=30, family="Arial"),
        )
        self.picker_label.grid(
            row=0,
            column=0,
            columnspan=3,
            padx=10,
            pady=10,
            sticky="nsew",
        )

        self.pick_file_btn = customtkinter.CTkButton(
            master=self,
            text="Pick files",
            command=self.open_file_dialog,
            font=self.button_style,
        )
        self.pick_file_btn.grid(
            column=0, columnspan=2, row=1, padx=30, pady=20, sticky="ew"
        )

        self.pick_dir_btn = customtkinter.CTkButton(
            master=self,
            text="Pick a folder",
            command=self.open_dir_dialog,
            font=self.button_style,
        )
        self.pick_dir_btn.grid(
            column=2, columnspan=2, row=1, padx=30, pady=20, sticky="ew"
        )

    def open_file_dialog(self) -> None:
        """
        Opens the file picker pop up
        gets the path to the file
        """
        self.file_path = customtkinter.filedialog.askopenfile()
        print(f"Selected path: {self.file_path.name}")

    def open_dir_dialog(self) -> None:
        """ """
        self.dir_path = customtkinter.filedialog.askdirectory()
        print(f"Selected path: {self.dir_path}")
