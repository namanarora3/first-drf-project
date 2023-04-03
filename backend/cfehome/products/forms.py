from django.forms import ModelForm
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        Model = Product
        fields = [
            'title',
            'content',
            'price'
        ]