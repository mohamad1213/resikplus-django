from django.urls import path
from .views import MyTokenObtainPairView, VerifyOTPAPIView, LogoutBlacklistTokenUpdateView, RegistrationAPIView, DemoView, DemoView2
# from backend.apps.accounts.views import LoginView, RegisterView, ProfileView, google_login, MyTokenObtainPairView, VerifyOTPAPIView, LogoutBlacklistTokenUpdateView, RegistrationAPIView, DemoView, DemoView2
from apps.accounts.views import *
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
urlpatterns = [
    # path("auth/login/", LoginView.as_view()),
    # path("auth/register/", RegisterView.as_view()),
    # path("me/", ProfileView.as_view()),
    # # urls.py
    # path("auth/google/", google_login),
    path("refresh/", TokenRefreshView.as_view()),
    path('auth/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('verify/', VerifyOTPAPIView.as_view(), name='verify-otp'),
    path('logout/', LogoutBlacklistTokenUpdateView.as_view(), name='logout'),
    path('register/', RegistrationAPIView.as_view(), name='registration'),
    path('experiment/',DemoView.as_view(),name='demo'),
    path('experiment2/',DemoView2.as_view(),name='demo2')
]

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns += router.urls


