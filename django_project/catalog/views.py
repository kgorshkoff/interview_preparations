from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView
from catalog.models import ProductItem
from catalog.forms import ProductForm


class ProductsListView(ListView):
    model = ProductItem
    template_name = 'index.html'

    def get_queryset(self):
        items = ProductItem.objects.all()
        return items


class ProductsAddView(CreateView):
    model = ProductItem
    form_class = ProductForm
    template_name = 'form.html'

    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)