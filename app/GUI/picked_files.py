"""Module defines a class PickedFilesFrame"""
from typing import List
import customtkinter


class PickedFilesFrame(customtkinter.CTkScrollableFrame):
    """Creates  a frame that displays the files picked"""

    def __init__(self, master, picked_files: List[str], **kwargs):
        super().__init__(master, **kwargs)

        self.display_files(picked_files)

    def display_files(self, picked_files: List[str]) -> None:
        """Displays the list of picked files in the frame"""

        self.file_list_labels = []

        for file in picked_files:
            self.file_list_label = customtkinter.CTkLabel(
                self,
                text=file,
                font=customtkinter.CTkFont(size=20),
                anchor="nw",
            )
            self.file_list_label.grid(
                row=len(self.file_list_labels), column=0, sticky="ew", pady=10, padx=20
            )
            self.file_list_labels.append(self.file_list_label)
