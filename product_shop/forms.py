from django import forms
from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['category', 'name', 'slug', 'image', 'description', 'price']
        widgets = {'description': forms.Textarea(attrs={'cols': 70})}