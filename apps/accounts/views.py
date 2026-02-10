from .serializers import RegisterSerializer, VerifyOTPSerializer, MyTokenObtainPairSerializer
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from apps.accounts.emails import send_otp
from apps.accounts.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.throttling import ScopedRateThrottle
from apps.accounts.utils import send_code_to_user
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    throttle_scope = 'login'
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    user = request.user
    user_role = "admin" if user.is_staff or user.is_superuser else "customer"
    
    return Response({
        'id': user.id,
        'email': user.email,
        'role': user_role,
        'full_name': user.get_full_name
    })
# class LoginTokenGenerationAPIView(APIView):
    
#     def post(self, request, *args, **kwargs):
#         serializer = LoginTokenGenerationSerializer(data=request.data)
#         data = {}

#         if serializer.is_valid(raise_exception=True):
            
#             email = serializer.data['email']
#             password = serializer.data['password']
#             user_obj = User.objects.get(email=email)
            

#             try:
#                 if user_obj is not None:
#                     access_token = AccessToken.for_user(user=user_obj)
#                     refresh_token = RefreshToken.for_user(user=user_obj)
#                     data['refresh'] = str(access_token)
#                     data['access'] = str(refresh_token)

#             except Exception as e:
#                 return Response({'message':'username or password is incorrect'})
            
#         return Response(data, status.HTTP_200_OK)

class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        user.is_active = True
        user.is_verified = True
        user.save()

        # send_code_to_user(user.email) # Skipped

        return Response({
            "data": serializer.data,
            "message": f"Hi {user.first_name}, user registered successfully. You can now login."
        }, status=status.HTTP_201_CREATED)

class VerifyOTPAPIView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        serializer = VerifyOTPSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data['email']
            otp = serializer.data['otp']
            user_obj = User.objects.get(email=email)
            
            if user_obj.otp == otp:
                user_obj.is_staff = True
                user_obj.save()
                return Response("verified")
            return Response(serializer.data,status.HTTP_400_BAD_REQUEST)


class LogoutBlacklistTokenUpdateView(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            
            return Response(status=status.HTTP_400_BAD_REQUEST)
class DemoView(APIView):
    # authentication_classes=[JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    
    def post(self,request):
        try:
            return Response("accessed")
        except Exception as e:
            print(e)
            return Response("")
class DemoView2(APIView):
    # authentication_classes=[JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self,request):
        try:
            return Response("accessed 2")
        except Exception as e:
            print(e)
            return Response("")
# from rest_framework_simplejwt.views import TokenObtainPairView
# from .serializers import  EmailTokenObtainPairSerializer
# from rest_framework.generics import CreateAPIView
# from rest_framework.permissions import AllowAny
# from .serializers import RegisterSerializer
# from rest_framework import generics, permissions
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .serializers import UserProfileSerializer
# # views.py
# from google.oauth2 import id_token
# from google.auth.transport import requests
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework_simplejwt.tokens import RefreshToken
# # views.py
# from django.contrib.auth import get_user_model
# User = get_user_model()

# from django.conf import settings


# @api_view(["POST"])
# def google_login(request):
#     token = request.data.get("token")  # ✅ WAJIB

#     if not token:
#         return Response(
#             {"error": "Token not provided"},
#             status=400
#         )

#     try:
#         info = id_token.verify_oauth2_token(
#             token,
#             requests.Request(),
#             settings.GOOGLE_CLIENT_ID
#         )

#         email = info["email"]
#         name = info.get("name", "")

#         user, _ = User.objects.get_or_create(
#             username=email,
#             defaults={
#                 "email": email,
#                 "first_name": name,
#             }
#         )

#         refresh = RefreshToken.for_user(user)

#         return Response({
#             "access": str(refresh.access_token),
#             "refresh": str(refresh),
#         })

#     except Exception as e:
#         print("GOOGLE LOGIN ERROR:", e)
#         return Response(
#             {"error": str(e)},
#             status=400
#         )

# class LoginView(TokenObtainPairView):
#     serializer_class = EmailTokenObtainPairSerializer

# class RegisterView(CreateAPIView):
#     serializer_class = RegisterSerializer
#     permission_classes = [AllowAny]
    


from rest_framework import viewsets
from .serializers import UserCRUDSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-data_joined')
    serializer_class = UserCRUDSerializer
    permission_classes = [permissions.IsAuthenticated] # Or IsAdminUser if strict


