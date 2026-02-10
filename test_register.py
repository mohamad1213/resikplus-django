import requests
import sys

URL = "http://127.0.0.1:8000/api/register/"
DATA = {
    "email": "testuser_no_email@resikplus.id",
    "password": "Password123!",
    "password2": "Password123!",
    "first_name": "Test",
    "last_name": "User"
}

try:
    print(f"Sending request to {URL}...")
    response = requests.post(URL, data=DATA)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
