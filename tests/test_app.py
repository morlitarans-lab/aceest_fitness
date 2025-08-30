import pytest
from app import create_app

@pytest.fixture()
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client

def test_index_ok(client):
    res = client.get("/")
    assert res.status_code == 200

def test_add_and_view_workouts(client):
    # start clean
    client.delete("/workouts")

    # invalid input
    res = client.post("/workouts", json={"workout": "", "duration": ""})
    assert res.status_code == 400

    # non-integer duration
    res = client.post("/workouts", json={"workout": "Run", "duration": "abc"})
    assert res.status_code == 400

    # valid add
    res = client.post("/workouts", json={"workout": "Run", "duration": 30})
    assert res.status_code == 201
    data = res.get_json()
    assert data["workout"] == "Run"
    assert data["duration"] == 30

    # view
    res = client.get("/workouts")
    assert res.status_code == 200
    data = res.get_json()
    assert data["count"] == 1
    assert data["items"][0]["workout"] == "Run"

def test_clear_workouts(client):
    client.post("/workouts", json={"workout": "Push-ups", "duration": 10})
    res = client.delete("/workouts")
    assert res.status_code == 200
    res = client.get("/workouts")
    assert res.get_json()["count"] == 0
