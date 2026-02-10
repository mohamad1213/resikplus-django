from django.db import models
from django.utils import timezone

class Partner(models.Model):
    TYPE_CHOICES = (
        ('Pengumpul', 'Pengumpul'),
        ('Pengolah', 'Pengolah'),
    )
    STATUS_CHOICES = (
        ('Aktif', 'Aktif'),
        ('Pending', 'Pending'),
        ('Nonaktif', 'Nonaktif'),
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
    join_date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
