[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
# PyShare
PyShare is a user-friendly and intuitive filesharing service built with CustomTkinter that allows users to easily share files with each other over the same network

## Installation

Clone or download the PyShare repository to your computer.

```sh
git clone git@github.com:musaubrian/pyshare

cd pyshare
```

### Setup

Run setup.py to well setup everything for you

```sh
python3 setup.py
```

## Usage

When PyShare launches, you will be prompted to choose whether you want to send or receive files.

### Sending Files

If you choose to send files:

- Select the files you want to send.
- PyShare will generate a pairing key that you will need to share with the recipient.
- Click the "Transfer" button.

### Receiving Files

If you choose to receive files:

- Enter the pairing key provided by the sender.
- Click the "Receive" button.
- PyShare will begin receiving the files and save them in `Desktop/pyshare_received`

## Tasks

- [x] Transfer text files

- [x] Transfer images

- [x] Transfer video?
> Transfers some types of video.
> Others won't because of an encoding error.

- [ ] Transfer audio
    - [x] mp4

    - [ ] mp3

## Issues

As of now,

- ~~Client can't receive the file if it the filename contains spaces.(one word files or files using snake_case)~~

- No indication if a file is being sent or received from the GUI
> Only shows after that the file has been sent on server. ON client it shows where the file has been saved.

- Currently slow when sending larger files

- Only transfers on file at a time. ~You have to disconnect to send a different one

### License

[MIT](./License)
