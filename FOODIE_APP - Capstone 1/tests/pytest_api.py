import requests

BASE_URL = "http://127.0.0.1:5000"

def test_user_registration():
    res = requests.post(
        f"{BASE_URL}/api/v1/users/register",
        json={"name": "Rahul"}
    )
    assert res.status_code == 201


def test_add_restaurant():
    res = requests.post(
        f"{BASE_URL}/api/v1/restaurants",
        json={"name": "Dominos", "location": "Bangalore"}
    )
    assert res.status_code == 201


def test_add_dish():
    res = requests.post(
        f"{BASE_URL}/api/v1/dishes",
        json={"name": "Pizza", "price": 299}
    )
    assert res.status_code == 201


def test_place_order():
    res = requests.post(
        f"{BASE_URL}/api/v1/orders",
        json={"user_id": 1, "dish_id": 1}
    )
    assert res.status_code == 201
