import time
import pytest
from pages.toolshop_page import ToolShopPage

def test_wipro_capstone_full_e2e(driver):
    driver.get("https://practicesoftwaretesting.com/")
    shop = ToolShopPage(driver)
    results = []

    try:
        shop.login("customer@practicesoftwaretesting.com", "welcome01")
        results.append("Attribute 1: User Login - PASSED")

        shop.search_and_add("Pliers")
        results.append("Attribute 2: Product Search - PASSED")
        results.append("Attribute 3: Add to Cart - PASSED")

        shop.manage_cart()
        results.append("Attribute 4: Cart Management (Update & Remove) - PASSED")

        shop.logout_user()
        results.append("Attribute 5: User Logout - PASSED")

    except Exception as e:
        print(f"\nTest failed during execution: {str(e)}")
        raise e

    print("\n" + "=" * 40)
    print("      WIPRO CAPSTONE FINAL REPORT")
    print("=" * 40)
    for status in results:
        print(status)
    print("=" * 40)
    print("ALL 5 ATTRIBUTES COMPLETED SUCCESSFULLY!")
    print("=" * 40)


# COMMAND TO RUN THIS - $env:PYTHONPATH="."; python -m pytest tests/test_search_flow.py -v -s