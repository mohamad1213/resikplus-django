from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = (
        ('Mesin', 'Mesin'),
        ('Alat', 'Alat'),
        ('Produk', 'Produk'),
        ('Bahan Baku', 'Bahan Baku'),
        ('Aksesoris', 'Aksesoris'),
        ('Lainnya', 'Lainnya'),
    )

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Produk')
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    stock_quantity = models.IntegerField(default=0)
    sku = models.CharField(max_length=100, blank=True, null=True)
    weight = models.CharField(max_length=50, blank=True, null=True)
    dimensions = models.CharField(max_length=100, blank=True, null=True)
    
    specs = models.JSONField(default=list, help_text="List of specifications", blank=True)
    rating = models.FloatField(default=0.0)
    reviews_count = models.IntegerField(default=0)
    in_stock = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
