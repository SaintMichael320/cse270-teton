
import requests


BASE_URL = "http://127.0.0.1:8000/users/"


def test_valid_login():
    params = {
        "username": "admin",
        "password": "qwerty",
    }

    response = requests.get(BASE_URL, params=params)

    assert response.status_code == 200


def test_invalid_login():
    params = {
        "username": "admin",
        "password": "admin",
    }

    response = requests.get(BASE_URL, params=params)

    assert response.status_code == 401
