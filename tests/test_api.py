import pytest
import requests
import json
import os

# Laad testdata uit JSON
def load_test_data():
    file_path = os.path.join(os.path.dirname(__file__), '../data/endpoints.json')
    with open(file_path, 'r') as file:
        return json.load(file)

# Data-driven met pytest
@pytest.mark.parametrize("test_case", load_test_data())
def test_api_response(test_case):
    url = test_case["endpoint"]
    expected_user_id = test_case["expected_user_id"]

    response = requests.get(url)

    # ✅ Validaties
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.headers["Content-Type"].startswith("application/json"), "Content-Type mismatch"
    json_data = response.json()
    assert json_data["userId"] == expected_user_id, f"Expected userId {expected_user_id}, got {json_data['userId']}"
