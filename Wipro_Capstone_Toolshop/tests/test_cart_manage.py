import pytest
from pages.toolshop_page import ToolShopPage


def test_cart_management_attribute(driver):
    driver.get("https://practicesoftwaretesting.com/")
    shop = ToolShopPage(driver)

    shop.search_and_add("Pliers")
    shop.manage_cart()

    print("\nAttribute 4: Cart Management (Update & Remove) - PASSED")