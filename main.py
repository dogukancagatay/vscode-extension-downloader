#!/usr/bin/env python3

import os
import time

from subprocess import check_output
from subprocess import PIPE, Popen

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from tqdm import tqdm

PAGE_LOAD_WAIT = 2  # seconds
EXTENSION_DOWNLOAD_WAIT = 2  # seconds
REMOTE_DRIVER_URL = os.getenv("REMOTE_DRIVER_URL", None)


def getExtensionListOld():
    command = ["code", "--list-extensions"]
    output = check_output(command).decode("utf-8")
    extensionList = output.split("\n")
    return extensionList


def getExtensionList():
    command = "code --list-extensions"
    with Popen(command, stdout=PIPE, stderr=None, shell=True) as process:
        output = process.communicate()[0].decode("utf-8")
        extensionList = output.split("\n")
        return extensionList


def downloadExtension(url, driver):
    driver.get(url)

    # print(f"Waiting for page to load: {url}")
    time.sleep(PAGE_LOAD_WAIT)

    driver.execute_script("window.scrollTo(0, 200)")

    try:
        elem = driver.find_element_by_xpath(
            '//button[normalize-space()="Download Extension"]'
        )
    except NoSuchElementException as e:
        # Hover on Download Extension span
        download_extension_dropdown = driver.find_element_by_xpath(
            '//span[normalize-space()="Download Extension"]'
        )
        hov = ActionChains(driver).move_to_element(download_extension_dropdown)
        hov.perform()

        # wait some moment
        time.sleep(0.5)
        # click on OS button
        elem = driver.find_element_by_xpath(
            '//li[@id="item-details-download-dropdown-list" and normalize-space()="Windows x64" ]'
        )

    elem.click()
    # print("Waiting for download")
    time.sleep(EXTENSION_DOWNLOAD_WAIT)


def main():
    EXT_URL_PREFIX = "https://marketplace.visualstudio.com/items?itemName="

    if REMOTE_DRIVER_URL is None:
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Remote(
            command_executor=REMOTE_DRIVER_URL,
            desired_capabilities=DesiredCapabilities.CHROME,
        )

    extensionList = getExtensionList()

    pbar = tqdm(extensionList)
    for extName in pbar:
        extName = extName.strip("\n\r\t ")

        if extName:
            pbar.set_description(f"Downloading {extName}")
            url = EXT_URL_PREFIX + extName
            downloadExtension(url, driver)

    driver.close()


if __name__ == "__main__":
    main()
