from django.forms import ModelForm
from catalog.models import ProductItem


class ProductForm(ModelForm):
    class Meta:
        model = ProductItem
        fields = ['title', 'price', 'vendor']
