from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    DESKTOPS_LINK = (By.LINK_TEXT, "Desktops")
    MAC_LINK = (By.LINK_TEXT, "Mac (1)")
    SORT_DROPDOWN = (By.ID, "input-sort")
    PRODUCT_IMAGE = (By.CSS_SELECTOR, ".image .img-responsive")
    ADD_TO_CART = (By.ID, "button-cart")
    SEARCH_BOX = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".fa-search")
    SEARCH_CRITERIA = (By.ID, "input-search")
    DESCRIPTION_CHECKBOX = (By.ID, "description")
    SEARCH_FINAL_BUTTON = (By.ID, "button-search")
    MAC_HEADING = (By.TAG_NAME, "h2")

    # Actions
    def click_desktops(self):
        self.driver.find_element(*self.DESKTOPS_LINK).click()

    def click_mac(self):
        self.driver.find_element(*self.MAC_LINK).click()

    def verify_mac_heading(self):
        heading = self.driver.find_element(*self.MAC_HEADING).text
        assert "Mac" in heading

    def sort_by_name_az(self):
        dropdown = Select(self.driver.find_element(*self.SORT_DROPDOWN))
        dropdown.select_by_visible_text("Name (A - Z)")

    def select_product_and_add_to_cart(self):
        self.driver.find_element(*self.PRODUCT_IMAGE).click()
        self.driver.find_element(*self.ADD_TO_CART).click()

    def search_product(self, product_name):
        search = self.driver.find_element(*self.SEARCH_BOX)
        search.clear()
        search.send_keys(product_name)
        self.driver.find_element(*self.SEARCH_BUTTON).click()

    def search_with_description(self, product_name):
        search_criteria = self.driver.find_element(*self.SEARCH_CRITERIA)
        search_criteria.clear()
        search_criteria.send_keys(product_name)

        checkbox = self.driver.find_element(*self.DESCRIPTION_CHECKBOX)
        if not checkbox.is_selected():
            checkbox.click()

        self.driver.find_element(*self.SEARCH_FINAL_BUTTON).click()
