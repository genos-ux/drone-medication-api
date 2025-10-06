from django.db import models

class Drone(models.Model):
    # Constants for choices
    MODEL_CHOICES = [
        ('Lightweight', 'Lightweight'),
        ('Middleweight', 'Middleweight'),
        ('Cruiserweight', 'Cruiserweight'),
        ('Heavyweight', 'Heavyweight'),
    ]

    STATE_CHOICES = [
        ('IDLE', 'IDLE'),
        ('LOADING', 'LOADING'),
        ('LOADED', 'LOADED'),
        ('DELIVERING', 'DELIVERING'),
        ('DELIVERED', 'DELIVERED'),
        ('RETURNING', 'RETURNING'),
    ]

    serial_number = models.CharField(max_length=100, primary_key=True)
    model = models.CharField(max_length=20, choices=MODEL_CHOICES)
    weight_limit = models.FloatField(default=500)
    battery_capacity = models.IntegerField(default=100) 
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='IDLE')

    def __str__(self):
        return f"{self.serial_number} ({self.model})"


class Medication(models.Model):
    name = models.CharField(max_length=255)
    weight = models.FloatField()
    code = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='medications/', blank=True, null=True)
    drone = models.ForeignKey(Drone, related_name='medications', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
