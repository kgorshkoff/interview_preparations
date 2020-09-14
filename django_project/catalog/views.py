from django.template.loader import render_to_string
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_html'] = render_to_string(self.template_name, {'form': self.form_class}, request=self.request)
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
