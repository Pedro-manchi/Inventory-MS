from django.forms import widgets
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta: {
        'product_id': 'product ID',
        'name': 'Name',
        'sku': 'SKU',
        'price': 'Price',
        'quantity': 'Quantity',
        'supplier': 'Supplier',
    }
    widgets = {
        'product_id': forms.NumberInput(attrs={'placeholder': 'e.g 1',
                                               'class':'form-control'}),
        'name': forms.TextInput(attrs={'placeholder': 'shirt',
                                               'class':'form-control'}),
        'sku': forms.TextInput(attrs={'placeholder': 'e.g s1234',
                                               'class':'form-control'}),
        'price': forms.NumberInput(attrs={'placeholder': 'e.g 29.9',
                                               'class':'form-control'}),
        'quantity': forms.NumberInput(attrs={'placeholder': 'e.g 100',
                                               'class':'form-control'}),
        'supplier': forms.TextInput(attrs={'placeholder': 'e.g fed Corp',
                                               'class':'form-control'})
    }