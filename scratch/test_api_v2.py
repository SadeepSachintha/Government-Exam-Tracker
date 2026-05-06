import requests
import json

API_URL = "https://applications.doenets.lk/doe_application/frontend/list-exams"
headers = {
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Referer': 'https://applications.doenets.lk/exams'
}

try:
    response = requests.get(API_URL, headers=headers, timeout=15)
    print(f"Status Code: {response.status_code}")
    print("Response Body (first 500 chars):")
    print(response.text[:500])
except Exception as e:
    print(f"Error: {e}")
