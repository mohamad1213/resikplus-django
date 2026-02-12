from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import date

class Partner(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='partner_profile')
    TYPE_CHOICES = (
        ('Individu', 'Individu'),
        ('UMKM', 'UMKM'),
        ('Organisasi', 'Organisasi'),
    )
    STATUS_CHOICES = (
        ('Aktif', 'Aktif'),
        ('Pending', 'Pending'),
        ('Ditolak', 'Ditolak'),
    )

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='Pengumpul')
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    join_date = models.DateField(default=date.today)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
