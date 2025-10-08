import pytest
from rest_framework.test import APIClient
from core.models import Drone

@pytest.mark.django_db
class TestDroneAPI:
    def setup_method(self):
        """Setup runs before every test."""
        self.client = APIClient()

        # Create sample drones
        self.drone_idle = Drone.objects.create(
            serial_number="DRONE_IDLE",
            model="Lightweight",
            weight_limit=300,
            battery_capacity=90,
            state="IDLE"
        )

        self.drone_low_battery = Drone.objects.create(
            serial_number="DRONE_LOW",
            model="Middleweight",
            weight_limit=300,
            battery_capacity=20,
            state="IDLE"
        )

        self.drone_delivering = Drone.objects.create(
            serial_number="DRONE_BUSY",
            model="Cruiserweight",
            weight_limit=500,
            battery_capacity=85,
            state="DELIVERING"
        )

    # Low battery test
    def test_low_battery_drone_cannot_be_loaded(self):
        payload = {"medications": [{"name": "Panadol", "weight": 50, "code": "P001"}]}
        response = self.client.post(
            f"/api/drones/{self.drone_low_battery.serial_number}/load/",
            payload,
            format="json"
        )

        assert response.status_code == 400  # type: ignore
        assert "battery" in str(response.data).lower()  # type: ignore

    # Weight limit validation
    def test_drone_cannot_exceed_weight_limit(self):
        payload = {"medications": [{"name": "HeavyMed", "weight": 400, "code": "H001"}]}
        response = self.client.post(
            f"/api/drones/{self.drone_idle.serial_number}/load/",
            payload,
            format="json"
        )

        assert response.status_code == 400  # type: ignore
        assert "weight" in str(response.data).lower()   # type: ignore

    # Successful medication load
    def test_drone_can_be_loaded_successfully(self):
        payload = {"medications": [{"name": "Paracetamol", "weight": 100, "code": "P002"}]}
        response = self.client.post(
            f"/api/drones/{self.drone_idle.serial_number}/load/",
            payload,
            format="json"
        )

        assert response.status_code in [200, 201]  # type: ignore
        assert "success" in str(response.data).lower() or "loaded" in str(response.data).lower() # type: ignore

    # Get battery level
    def test_get_drone_battery_level(self):
        response = self.client.get(f"/api/drones/{self.drone_idle.serial_number}/battery/")
        assert response.status_code == 200  # type: ignore
        assert response.data["battery_capacity"] == 90  # type: ignore

    # Get available drones
    def test_get_available_drones(self):
        response = self.client.get("/api/drones/available/")
        assert response.status_code == 200  # type: ignore
        serial_numbers = [drone["serial_number"] for drone in response.data]  # type: ignore
        assert self.drone_idle.serial_number in serial_numbers
        assert self.drone_delivering.serial_number not in serial_numbers
