from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DroneViewSet, MedicationViewSet
from django.http import HttpResponse

router = DefaultRouter()
router.register(r'drones', DroneViewSet, basename='drone')
router.register(r'medications', MedicationViewSet, basename='medication')

def home(request):
    return HttpResponse("<h1>Welcome to Drone API 🚀</h1><p>Go to <a href='/admin/'>Admin Dashboard</a></p>")

urlpatterns = [
    path('/', home), 
    path('', include(router.urls)),
]

# add media uploads for medication images (so the image field actually works)

# or write unit tests for your validation logic.