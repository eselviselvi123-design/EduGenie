
def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200


def test_health_endpoint(client):
    response = client.get("/api/health")
    assert response.status_code == 200

    data = response.get_json()
    assert data["status"] == "success"


def test_learn_endpoint(client, monkeypatch):
    import main

    monkeypatch.setattr(
        main,
        "explain_topic",
        lambda topic, level="Beginner": "Test explanation"
    )

    response = client.post(
        "/api/learn",
        json={"topic": "Python", "level": "Beginner"}
    )

    assert response.status_code == 200
    assert response.get_json()["result"] == "Test explanation"