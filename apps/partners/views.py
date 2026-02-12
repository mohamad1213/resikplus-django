from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Partner
from .serializers import PartnerSerializer
from django.contrib.auth import get_user_model
from django.db import transaction

User = get_user_model()

class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all().order_by('-created_at')
    serializer_class = PartnerSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]

    @action(detail=True, methods=['post'])
    def verify(self, request, pk=None):
        partner = self.get_object()
        
        if partner.status == 'Aktif':
            return Response({'message': 'Mitra sudah aktif', 'status': 'Aktif'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            with transaction.atomic():
                # 1. Update Status
                partner.status = 'Aktif'
                
                # 2. Check if user already linked or email exists
                message_details = ""
                credentials = None
                
                if not partner.user:
                    email = partner.email
                    if not email:
                        return Response({'error': 'Mitra ini tidak memiliki email untuk dibuatkan akun.'}, status=status.HTTP_400_BAD_REQUEST)

                    existing_user = User.objects.filter(email=email).first()
                    
                    if existing_user:
                        partner.user = existing_user
                        message_details = "Akun pengguna ditautkan dengan email yang sudah ada."
                    else:
                        # Create new user
                        # Generate simple default password or random one
                        default_password = "ResikPlusPartner!123"
                        new_user = User.objects.create_user(
                            email=email,
                            first_name=partner.name[:30], # Truncate if too long (max 150 usually)
                            password=default_password
                        )
                        new_user.is_active = True
                        # new_user.is_staff = False # Ensure not admin
                        new_user.save()
                        
                        partner.user = new_user
                        credentials = {'email': email, 'password': default_password}
                        message_details = f"Akun baru berhasil dibuat. Password default: {default_password}"
                
                partner.save()
                
                return Response({
                    'status': 'Aktif',
                    'message': f"Mitra berhasil diverifikasi. {message_details}",
                    'credentials': credentials
                })
                
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
