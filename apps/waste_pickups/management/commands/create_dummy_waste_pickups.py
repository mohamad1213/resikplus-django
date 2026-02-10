from django.core.management.base import BaseCommand
from django.utils import timezone
from apps.waste_pickups.models import WastePickup
from apps.partners.models import Partner
import random
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate dummy waste pickups'

    def handle(self, *args, **kwargs):
        WastePickup.objects.all().delete()
        
        partner, created = Partner.objects.get_or_create(
            name="Mitra Resik",
            defaults={'contact_person': 'Budi', 'phone': '08123456789', 'status': 'Aktif'}
        )
        if not created and partner.status != 'Aktif':
            partner.status = 'Aktif'
            partner.save()
            
        partner2, created = Partner.objects.get_or_create(
            name="Bank Sampah Jaya",
            defaults={'contact_person': 'Siti', 'phone': '08123456788', 'status': 'Aktif'}
        )
        if not created and partner2.status != 'Aktif':
            partner2.status = 'Aktif'
            partner2.save()
        partners = [partner, partner2]

        statuses = ['pending', 'confirmed', 'in_progress', 'completed', 'cancelled']
        waste_types = ['Plastik', 'Kertas/Kardus', 'Logam', 'Kaca', 'Elektronik', 'Organik', 'B3 (Bahan Berbahaya)', 'Campuran']

        for i in range(10):
            status = random.choice(statuses)
            scheduled_date = timezone.now().date() + timedelta(days=random.randint(1, 14))
            completed_date = None
            if status == 'completed':
                completed_date = scheduled_date + timedelta(days=1)
            
            WastePickup.objects.create(
                customer_name=f"Customer {i+1}",
                customer_phone=f"0812345678{i}",
                customer_email=f"customer{i+1}@example.com",
                address=f"Jalan Contoh No. {i+1}",
                waste_type=random.choice(waste_types),
                estimated_weight=random.randint(10, 100),
                actual_weight=random.randint(10, 100) if status == 'completed' else None,
                partner=random.choice(partners),
                status=status,
                scheduled_date=scheduled_date,
                completed_date=completed_date,
                price=random.randint(50000, 500000),
                notes="Contoh catatan"
            )
        
        self.stdout.write(self.style.SUCCESS('Successfully populated dummy waste pickups'))
