from django.db import models
from django.core.exceptions import ValidationError

def validate_sku(value):
    if not value.endswith("@gmail.com"):
        raise ValidationError("This field accepts only Gmail addresses.")

class Product(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=50, unique=True, validators=[validate_sku])
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
