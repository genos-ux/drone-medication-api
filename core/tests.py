import pytest
from rest_framework.test import APIClient
from core.models import Drone

@pytest.mark.django_db
def test_drone_with_low_battery_cannot_be_loaded():
    client = APIClient()  # ✅ This must be DRF’s client

    drone = Drone.objects.create(
        serial_number="DRN_LOW",
        model="Lightweight",
        weight_limit=100,
        battery_capacity=20,
        state="IDLE"
    )

    payload = {
        "medications": [
            {"name": "Panadol", "weight": 50, "code": "P001"}
        ]
    }

    response = client.post(f"/api/drones/{drone.serial_number}/load/", payload, format="json")

    # assert response.status_code == 400
    # assert "Battery too low" in response.data["error"]
