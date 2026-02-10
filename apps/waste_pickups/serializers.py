from rest_framework import serializers
from .models import WastePickup
from apps.partners.models import Partner

class WastePickupSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    customerName = serializers.CharField(source='customer_name')
    customerPhone = serializers.CharField(source='customer_phone')
    customerEmail = serializers.EmailField(source='customer_email', required=False, allow_null=True)
    wasteType = serializers.CharField(source='waste_type')
    estimatedWeight = serializers.DecimalField(source='estimated_weight', max_digits=10, decimal_places=2)
    actualWeight = serializers.DecimalField(source='actual_weight', max_digits=10, decimal_places=2, required=False, allow_null=True)
    partnerId = serializers.PrimaryKeyRelatedField(source='partner', queryset=Partner.objects.all(), required=False, allow_null=True)
    partnerName = serializers.CharField(source='partner.name', read_only=True)
    scheduledDate = serializers.DateField(source='scheduled_date', required=False, allow_null=True)
    completedDate = serializers.DateField(source='completed_date', required=False, allow_null=True)
    createdAt = serializers.DateTimeField(source='created_at', format="%Y-%m-%d", read_only=True)

    class Meta:
        model = WastePickup
        fields = [
            'id', 'customerName', 'customerPhone', 'customerEmail', 'address',
            'wasteType', 'estimatedWeight', 'actualWeight', 'partnerId',
            'partnerName', 'status', 'scheduledDate', 'completedDate',
            'price', 'notes', 'createdAt'
        ]
