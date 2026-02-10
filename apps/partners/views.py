from rest_framework import viewsets
from .models import Partner
from .serializers import PartnerSerializer

class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all().order_by('-created_at')
    serializer_class = PartnerSerializer
