#!/usr/bin/env python3

import os
from pathlib import Path
import subprocess

def create_pyshare_dir():
    """Creates a directory where the received files will be stored"""
    dir_name = "pyshare_received"
    home_path = Path.home()
    full_path = Path(os.path.join(home_path, dir_name))
    if full_path.exists() is False:
        # change to home and create the directory
        os.chdir(home_path)
        os.mkdir(dir_name)
    else:
        raise FileExistsError

def install_deps():
    """Install dependencies from te requirements.txt"""
    try:
        subprocess.call(["pip3", "install", "-r", "requirements.txt"])
    except:
        print("Pip might not be installed")


if __name__ == "__main__":
    create_pyshare_dir()
    install_deps()
