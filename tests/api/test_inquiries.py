
from sqlalchemy import text


def test_db_session_can_query_database(db_session):
    result = db_session.execute(text("SELECT 1")).scalar_one()

    assert result == 1


def test_create_inquiry(client):
    payload = {
        "name": "Ali Khan",
        "contact_number": "+923001234567",
        "destination": "Kandy, Sri Lanka",
        "number_of_travelers": 2,
        "duration_days": 7,
    }

    response = client.post("/api/v1/inquiries", json=payload)

    assert response.status_code == 200

    data = response.json()
    assert data["id"] > 0
    assert data["name"] == "Ali Khan"
    assert data["destination"] == "Kandy, Sri Lanka"
    assert data["status"] == "new"
    assert data["created_at"] is not None


def test_get_existing_inquiry(client):
    payload = {
        "name": "Sara Ahmed",
        "contact_number": "+923001112233",
        "destination": "Ella, Sri Lanka",
        "number_of_travelers": 3,
        "duration_days": 5,
    }

    created = client.post("/api/v1/inquiries", json=payload)
    assert created.status_code == 200
    
    inquiry_id = created.json()["id"]

    response = client.get(f"/api/v1/inquiries/{inquiry_id}")

    assert response.status_code == 200
    assert response.json()["id"] == inquiry_id
    assert response.json()["name"] == "Sara Ahmed"


def test_get_missing_inquiry_returns_404(client):
    response = client.get("/api/v1/inquiries/99999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Booking inquiry not found"


def test_invalid_traveler_count_is_rejected(client):
    payload = {
        "name": "Ali Khan",
        "contact_number": "+923001234567",
        "destination": "Kandy",
        "number_of_travelers": 0,
        "duration_days": 7,
    }

    response = client.post("/api/v1/inquiries", json=payload)

    assert response.status_code == 422

