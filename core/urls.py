from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from api.views import EmailLoginView
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/auth/login/", EmailLoginView.as_view()),
    path("api/auth/refresh/", TokenRefreshView.as_view()),
    path("api/", include("api.urls")),
    path("api/education/", include("education.urls")),
]
