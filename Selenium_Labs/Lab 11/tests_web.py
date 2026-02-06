import pytest
from selenium import webdriver
from pages import HomePage
import time


class TestTutorialsNinja:

    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://tutorialsninja.com/demo/")
        self.home = HomePage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_lab3_and_lab4_flow(self):
        # Verify title
        assert "Your Store" in self.driver.title

        # Lab 3 + Lab 4 flow
        self.home.click_desktops()
        time.sleep(1)

        self.home.click_mac()
        time.sleep(1)

        self.home.verify_mac_heading()

        self.home.sort_by_name_az()
        time.sleep(1)

        self.home.select_product_and_add_to_cart()
        time.sleep(2)

        self.home.search_product("Monitors")
        time.sleep(2)

        self.home.search_with_description("Monitors")
        time.sleep(2)

        print("Lab 3 & Lab 4 executed using POM successfully!")
