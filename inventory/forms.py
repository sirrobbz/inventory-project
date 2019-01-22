from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'cetagory', 'supplier', 'unit_price', 'description', 'received', 'issued', 'balance')