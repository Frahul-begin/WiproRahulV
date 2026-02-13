import requests
import pytest

BASE_URL = "http://127.0.0.1:5000/api"

@pytest.fixture
def new_movie():
    return {
        "id": 103,
        "movie_name": "Salaar",
        "language": "Telugu",
        "duration": "2h 55m",
        "price": 300
    }

def test_get_all_movies():
    response = requests.get(f"{BASE_URL}/movies")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_movie_by_id():
    response = requests.get(f"{BASE_URL}/movies/101")
    assert response.status_code == 200
    assert response.json()["movie_name"] == "The Godfather"

def test_add_movie(new_movie):
    response = requests.post(f"{BASE_URL}/movies", json=new_movie)
    assert response.status_code == 201

def test_update_movie():
    update_data = {"price": 350}
    response = requests.put(f"{BASE_URL}/movies/103", json=update_data)
    assert response.status_code == 200

def test_delete_movie():
    response = requests.delete(f"{BASE_URL}/movies/103")
    assert response.status_code == 200

def test_book_tickets():
    booking_data = {"movie_id": 101, "tickets": 2}
    response = requests.post(f"{BASE_URL}/bookings", json=booking_data)
    assert response.status_code == 201
    assert response.json()["total_price"] == 500
