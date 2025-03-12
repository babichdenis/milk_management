from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'volume', 'expiration_date',
                  'production_cost', 'category']
