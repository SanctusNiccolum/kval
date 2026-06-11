from django.contrib import admin
from .models import Product
from.forms import ProductForm

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    form = ProductForm
    
