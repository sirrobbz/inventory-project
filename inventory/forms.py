from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('date', 'name', 'whom', 'requisition', 'unit_price', 'description', 'received', 'issued', 'balance')
        widgets = {'date': forms.DateTimeInput(attrs={'class': 'datetime-input'})}
