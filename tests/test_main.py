import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_integration_json():
    """Test if /integration-json returns expected JSON structure"""
    response = client.get("/integration-json")
    assert response.status_code == 200
    json_data = response.json()
    
    assert "data" in json_data
    assert "date" in json_data["data"]
    assert "descriptions" in json_data["data"]
    assert "integration_category" in json_data["data"]
    assert "integration_type" in json_data["data"]
    assert "settings" in json_data["data"]
    
    assert json_data["data"]["integration_type"] == "output"
    assert isinstance(json_data["data"]["is_active"], bool)
    assert isinstance(json_data["data"]["output"], list)

@patch("requests.get")
def test_exercise_endpoint(mock_get):
    """Mock API call for /exe and test response"""
    mock_response = [{"name": "Squat", "muscle": "glutes", "equipment": "body only"}]
    mock_get.return_value = MockResponse(mock_response, 200)

    response = client.get("/exe")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self._status_code = status_code

    def json(self):
        return self.json_data 

    @property
    def status_code(self):
        return self._status_code
