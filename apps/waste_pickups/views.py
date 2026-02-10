from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import WastePickup
from .serializers import WastePickupSerializer
from rest_framework.decorators import action

class WastePickupViewSet(viewsets.ModelViewSet):
    queryset = WastePickup.objects.all().order_by('-created_at')
    serializer_class = WastePickupSerializer

    # Optional: Filter by status
    def get_queryset(self):
        queryset = super().get_queryset()
        status_param = self.request.query_params.get('status')
        if status_param:
            queryset = queryset.filter(status=status_param)
        return queryset
