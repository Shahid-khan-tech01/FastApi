from fastapi.testclient import TestClient
from apitesting import app

client = TestClient(app)

# Test Home Api :
def test_home():
    response = client.get("/")
    # Status Code check 
    assert response.status_code == 200
    # Request Body Check 
    assert response.json() == {"message": "Hello Shahid bro"}

# Test Add Api :
def test_add():
    response = client.get("/add?a=5&b=4")
    assert response.status_code == 200
    assert response.json() == {"result": 9}