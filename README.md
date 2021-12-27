# VSCode Extension Downloader

This is an Selenium based downloader of extensions installed on your Visual Studio Code for offline usage.

Basically, it runs `code --list-extensions`, go to the web page of the extensions one by one and clicks on download link.

To download in the background, a remote Selenium Chrome node can be run(`docker-compose.yml`).


## Running

A recent version of Python 3 and Docker (if you don't use local chrome driver) are required.

### Running using containerized Chrome Driver (recommended)

Run Selenium Chrome node.

```sh
docker-compose up -d
```

Install Python requirements.

```sh
pip3 install --user -r requirements.txt
```

Run *main.py* with remote web driver address.

```sh
REMOTE_DRIVER_URL=http://localhost:4444/wd/hub ./main.py
```

This approach downloads all extensions into *downloads* directory inside the same directory.

### Running using local Chrome Driver

It is required to install Chrome driver on you computer, and add it to *PATH*.

```sh
brew install --cask chromedriver
```

Install Python requirements.

```sh
pip3 install --user -r requirements.txt
```

Run *main.py*

```sh
./main.py
```

Extensions will be on your *Downloads* folder. Beware of the fact that, the Selenium Chrome driver is affected by your mouse moves, it is recommended that you don't use your computer during download process.

## Note

- Most of the VSCode extensions doesn't have any native dependency, if some of your extensions have (e.g. [redhat.java](https://marketplace.visualstudio.com/items?itemName=redhat.java)), the `main.py` script will download the one for the `Windows x64` which can be configured in the source code.
