import pytest
import csv
import os
from pages.toolshop_page import ToolShopPage

def get_csv_data():
    data = []
    path = os.path.join(os.getcwd(), 'test_data.csv')
    with open(path, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append((row['email'], row['password'], row['product']))
    return data

@pytest.mark.parametrize("email, password, product", get_csv_data())
def test_wipro_capstone_flow(driver, email, password, product):
    shop = ToolShopPage(driver)
    shop.login(email, password)
    shop.search_and_view_details(product)
    shop.add_product_to_cart()
    shop.update_and_remove_cart_item()
    shop.logout_user()


#  pytest tests/test_csv_driven.py --html=results/pytest_report.html --self-contained-html