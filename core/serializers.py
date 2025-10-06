from rest_framework import serializers
from .models import Drone, Medication


class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'

    def validate_name(self, value):
        """
        Medication name can only contain letters, numbers, hyphens, and underscores.
        """
        import re
        if not re.match(r'^[A-Za-z0-9_-]+$', value):
            raise serializers.ValidationError(
                "Name can only contain letters, numbers, hyphens, and underscores."
            )
        return value

    def validate_weight(self, value):
        """
        Medication weight must be positive.
        """
        if value <= 0:
            raise serializers.ValidationError("Weight must be greater than zero.")
        return value


class DroneSerializer(serializers.ModelSerializer):
    medications = MedicationSerializer(many=True, read_only=True)

    class Meta:
        model = Drone
        fields = '__all__'

    def validate_weight_limit(self, value):
        """
        Drones cannot have a weight limit above 500g.
        """
        if value > 500:
            raise serializers.ValidationError("Maximum weight limit is 500 grams.")
        return value

    def validate_battery_capacity(self, value):
        """
        Battery capacity must be between 0 and 100.
        """
        if value < 0 or value > 100:
            raise serializers.ValidationError("Battery capacity must be between 0 and 100.")
        return value

    def validate(self, attrs):
        state = attrs.get('state')
        battery = attrs.get('battery_capacity')

        if state == 'LOADING' and battery < 25:
            raise serializers.ValidationError("Cannot load drone with battery below 25%.")
        return attrs
