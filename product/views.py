from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product

# Create your views here.

class IndexListView(ListView):
    model = Product
    queryset = Product.objects.filter(is_active=True)
    template_name = "products/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        return context

class ProductListView(ListView):
    model = Product
    queryset = Product.objects.filter(is_active=True)
    template_name = "products/show_products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        return context
