from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DroneViewSet, MedicationViewSet

router = DefaultRouter()
router.register(r'drones', DroneViewSet, basename='drone')
router.register(r'medications', MedicationViewSet, basename='medication')

urlpatterns = [
    path('', include(router.urls)),
]

# add media uploads for medication images (so the image field actually works)

# or write unit tests for your validation logic.