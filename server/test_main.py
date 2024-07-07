from main import app
from fastapi.testclient import TestClient

client = TestClient(app=app)

# Test the API endpoint to add new feedback data to the database
def test_add_feedback_main():
    response = client.post(
        "/feedbacks",
        headers={
            "accept": "application/json",
            "Content-Type": "application/json"
        },
        json={
            "rating": 4
        }
    )
    assert response.status_code == 201 # if the response's status code equals to 201, then it is correct

# Please uncomment the function below to test the get_feedbacks() API
# For some reason, I could not do multiple API endpoint tests as it would cause an error
# I have looked up and tried every solutions from the internet, such as trying to use pytest-asyncio, anyio, etc, yet they did not work
# The error seemed to be cause by a stopped event loop in asyncio library

# def test_get_feedbacks_main():
#     response = client.get("/feedbacks")
#     assert response.status_code == 200 # if the status code equals to 200, then the get_feedbacks() API endpoint successfully finishes its job