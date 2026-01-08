from django.urls import path
from .views import *

urlpatterns = [
    path("health/", health_check),
]
