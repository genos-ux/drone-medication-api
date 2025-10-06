from django.core.management.base import BaseCommand
from core.models import Drone, Medication
import random

class Command(BaseCommand):
    help = "Seeds the database with sample drones and medications."

    def handle(self, *args, **kwargs):
        Drone.objects.all().delete()
        Medication.objects.all().delete()

        models = ["Lightweight", "Middleweight", "Cruiserweight", "Heavyweight"]
        states = ["IDLE", "LOADING", "LOADED", "DELIVERING", "DELIVERED", "RETURNING"]

        # Create sample drones
        drones = []
        for i in range(5):
            drone = Drone.objects.create(
                serial_number=f"DRN00{i+1}",
                model=random.choice(models),
                battery_capacity=random.randint(25, 100),
                state=random.choice(states)
            )
            drones.append(drone)

        meds = [
            {"name": "Paracetamol", "weight": 50, "code": "PARA001"},
            {"name": "Ibuprofen", "weight": 80, "code": "IBU002"},
            {"name": "Cefuroxime", "weight": 100, "code": "CEF003"},
            {"name": "Amoxicillin", "weight": 90, "code": "AMOX004"},
            {"name": "Azithromycin", "weight": 60, "code": "AZI005"},
        ]

        for med in meds:
            Medication.objects.create(
                name=med["name"],
                weight=med["weight"],
                code=med["code"],
                drone=random.choice(drones)
            )

        self.stdout.write(self.style.SUCCESS("✅ Sample drones and medications added successfully!"))
