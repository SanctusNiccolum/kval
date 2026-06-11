from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
