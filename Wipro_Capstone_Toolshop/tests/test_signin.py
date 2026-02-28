import pytest
from pages.toolshop_page import ToolShopPage


def test_signin_attribute(driver):
    driver.get("https://practicesoftwaretesting.com/")
    shop = ToolShopPage(driver)

    shop.click(shop.SIGN_IN_NAV)
    shop.type_text(shop.EMAIL_FIELD, "customer@practicesoftwaretesting.com")
    shop.type_text(shop.PASSWORD_FIELD, "welcome01")
    shop.click(shop.LOGIN_BTN)

    print("\nACTION: Sign-in submitted.")

# COMMAND TO RUN THIS - $env:PYTHONPATH="."; python -m pytest tests/test_signin.py -v -s