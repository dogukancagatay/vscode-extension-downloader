# VSCode Extension Downloader

This is an Selenium based downloader of extensions installed on your Visual Studio Code for offline usage.

To download in the background, a Selenium Chrome node can be run (`docker-compose.yml`) in the background.

## Running

Python 3 and Docker (if you don't use local chrome driver) are required.

First of all, you need a list of extensions `extensions-list.txt`. Following command creates a list from your local VSCode installation.

```sh
./update-list.sh
```

Afterwards, you can choose the way you run.

### Quick start with containers

Run Selenium Chrome node along with VNC viewer.

```sh
docker-compose up -d selenium vnc
```

Build the container image of the app and run.

```sh
docker-compose build
docker-compose run app
```

You can see the progress from application logs. Or open the VNC viewer for action [http://localhost:8081/vnc.html]().

### Running locally using containerized Chrome Driver (recommended)

Run Selenium Chrome node.

```sh
docker-compose up -d
```

Install Python requirements.

```sh
pip3 install --user -r requirements.txt
```

Run _main.py_ with remote web driver address.

```sh
REMOTE_DRIVER_URL=http://localhost:4444/wd/hub ./main.py
```

This approach downloads all extensions into _downloads_ directory inside the same directory.

### Running using local Chrome Driver

It is required to install Chrome driver on you computer, and add it to _PATH_.

```sh
brew install --cask chromedriver
```

Install Python requirements.

```sh
pip3 install --user -r requirements.txt
```

Run _main.py_

```sh
./main.py
```

Extensions will be on your _Downloads_ folder. Beware of the fact that, the Selenium Chrome driver is affected by your mouse moves, it is recommended that you don't interrupt its operation during download process.

## Note

- Most of the VSCode extensions doesn't have any native dependency, if some of your extensions have (e.g. [redhat.java](https://marketplace.visualstudio.com/items?itemName=redhat.java)), the `main.py` script will download the one for the `Windows x64` which can be configured with `OS_LABEL` environment variable.
