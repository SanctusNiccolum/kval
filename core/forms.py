from django.forms import ModelForm, ValidationError
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "category",
            "price",
            "sku",
        ]

    def clean_price(self):
        cleaned_data = super().clean()
        price = cleaned_data.get('price')
        if price <= 0:
            raise ValidationError('ты долбаёб, цена не может быть отрицательной')
        return price
        