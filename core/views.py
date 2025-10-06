from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Drone, Medication
from .serializers import DroneSerializer, MedicationSerializer


class DroneViewSet(viewsets.ModelViewSet):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    lookup_field = 'serial_number'

    # Custom endpoint: get battery level
    @action(detail=True, methods=['get'])
    def battery(self, request, pk=None):
        drone = self.get_object()
        return Response({"battery_capacity": drone.battery_capacity})

    # Custom endpoint: list available drones for loading
    @action(detail=False, methods=['get'])
    def available(self, request):
        available_drones = Drone.objects.filter(state='IDLE', battery_capacity__gte=25)
        serializer = self.get_serializer(available_drones, many=True)
        return Response(serializer.data)

    # Custom endpoint: load medications onto a drone
    @action(detail=True, methods=['post'])
    def load(self, request, pk=None):
        drone = self.get_object()
        if drone.battery_capacity < 25:
            return Response(
                {"error": "Cannot load drone with battery below 25%."},
                status=status.HTTP_400_BAD_REQUEST
            )

        meds_data = request.data.get('medications', [])
        total_weight = sum(m['weight'] for m in meds_data)

        for med in meds_data:
            med['drone'] = drone.id
            serializer = MedicationSerializer(data=med)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        if total_weight > drone.weight_limit:
            return Response(
                {"error": f"Total weight {total_weight} exceeds drone limit of {drone.weight_limit}."},
                status=status.HTTP_400_BAD_REQUEST
            )

        drone.state = 'LOADED'
        drone.save()
        return Response({"message": "Drone loaded successfully."},status=status.HTTP_200_OK)


class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
