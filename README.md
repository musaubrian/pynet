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

- [ ] Transfer video?

## Issues

As of now,

- [x] Client can't receive the file if it the filename contains spaces.(one word files or files using snake_case)

- [ ] No indication if a file is being sent or received from the GUI

- [ ] Currently slow when sending larger files

### License

[MIT](./License)
