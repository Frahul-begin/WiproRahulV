from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

GRIDURL = "http://192.168.198.1:4444/wd/hub"


def getdriver(browser):
    if browser == "chrome":
        capabilities = DesiredCapabilities.CHROME.copy()
    elif browser == "firefox":
        capabilities = DesiredCapabilities.FIREFOX.copy()
    else:
        raise ValueError("Browser not supported")
    driver = webdriver.Remote(
        command_executor=GRIDURL,
        desired_capabilities=capabilities

    )
    driver.maximize_window()
    return driver
