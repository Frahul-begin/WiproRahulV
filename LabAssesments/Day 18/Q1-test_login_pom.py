import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# BASE PAGE
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by, locator):
        self.driver.find_element(by, locator).click()

    def type_text(self, by, locator, value):
        self.driver.find_element(by, locator).clear()
        self.driver.find_element(by, locator).send_keys(value)

    def get_text(self, by, locator):
        return self.driver.find_element(by, locator).text


# LOGIN PAGE
class LoginPage(BasePage):

    EMAIL = (By.ID, "input-email")
    PASSWORD = (By.ID, "input-password")
    LOGIN_BTN = (By.XPATH, "//input[@value='Login']")
    ERROR_MSG = (By.CSS_SELECTOR, ".alert-danger")

    def login(self, email, password):
        self.type_text(*self.EMAIL, email)
        self.type_text(*self.PASSWORD, password)
        self.click(*self.LOGIN_BTN)

    def get_error_message(self):
        return self.get_text(*self.ERROR_MSG)


# TEST SCRIPT
def test_invalid_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.LINK_TEXT, "My Account").click()
    driver.find_element(By.LINK_TEXT, "Login").click()

    login_page = LoginPage(driver)
    login_page.login("test@test.com", "wrongpass")

    assert "Warning" in login_page.get_error_message()
    print("✅ Test Passed: Invalid login warning displayed")

    driver.quit()
