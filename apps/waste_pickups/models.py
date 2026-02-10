from django.db import models
from django.utils import timezone
from apps.partners.models import Partner

class WastePickup(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Menunggu'),
        ('confirmed', 'Dikonfirmasi'),
        ('in_progress', 'Dalam Proses'),
        ('completed', 'Selesai'),
        ('cancelled', 'Dibatalkan'),
    )

    WASTE_TYPE_CHOICES = (
        ('Plastik', 'Plastik'),
        ('Kertas/Kardus', 'Kertas/Kardus'),
        ('Logam', 'Logam'),
        ('Kaca', 'Kaca'),
        ('Elektronik', 'Elektronik'),
        ('Organik', 'Organik'),
        ('B3 (Bahan Berbahaya)', 'B3 (Bahan Berbahaya)'),
        ('Campuran', 'Campuran'),
    )

    customer_name = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=50)
    customer_email = models.EmailField(blank=True, null=True)
    address = models.TextField()
    waste_type = models.CharField(max_length=50, choices=WASTE_TYPE_CHOICES)
    estimated_weight = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    actual_weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    partner = models.ForeignKey(Partner, on_delete=models.SET_NULL, null=True, related_name='waste_pickups')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    scheduled_date = models.DateField(null=True, blank=True)
    completed_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_name} - {self.waste_type} ({self.status})"
