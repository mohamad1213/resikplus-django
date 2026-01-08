from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import generics
from .models import *
from .serializers import *
@api_view(["GET"])
def health_check(request):
    return Response({"status": "ok"})
# View for email-based login
class EmailLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = EmailLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)



