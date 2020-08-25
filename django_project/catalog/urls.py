from django.urls import path
from catalog.views import ProductsListView, ProductsAddView

urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),
    path('add/', ProductsAddView.as_view(), name='add')
]