from django.forms import ModelForm
from catalog.models import ProductItem


class ProductForm(ModelForm):
    class Meta:
        model = ProductItem
        fields = ['title', 'price', 'vendor']

        def __init__(self, *args, **kwargs):
            super(ProductForm, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'
                field.help_text = ''
