import pytest
import csv
from pages.toolshop_page import ToolShopPage


def get_csv_data():
    data = []
    with open('test_data.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append((row['email'], row['password'], row['product']))
    return data


@pytest.mark.parametrize("user, pwd, item", get_csv_data())
def test_csv_driven_flow(driver, user, pwd, item):
    driver.get("https://practicesoftwaretesting.com/")
    shop = ToolShopPage(driver)

    shop.login(user, pwd)
    shop.search_and_add(item)
    print(f"Tested with: {user} and {item}")