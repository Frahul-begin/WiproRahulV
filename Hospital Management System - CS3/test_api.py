import requests
import pytest

BASE_URL = "http://127.0.0.1:5000/api"

@pytest.fixture
def patient_data():
    return {
        "name": "Rahul",
        "age": 24,
        "gender": "Male",
        "contact": "9876543210",
        "disease": "Fever",
        "doctor": "Dr. Smith"
    }

def test_register_patient(patient_data):
    response = requests.post(f"{BASE_URL}/patients", json=patient_data)
    assert response.status_code == 201

def test_get_patients():
    response = requests.get(f"{BASE_URL}/patients")
    assert response.status_code == 200

def test_get_invalid_patient():
    response = requests.get(f"{BASE_URL}/patients/999")
    assert response.status_code == 404
