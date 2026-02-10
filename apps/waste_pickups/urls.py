from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WastePickupViewSet

router = DefaultRouter()
router.register(r'waste-pickups', WastePickupViewSet, basename='waste_pickup')

urlpatterns = [
    path('', include(router.urls)),
]
