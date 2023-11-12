from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Order

# Create your views here.
class CartView(TemplateView):
    model = Order
    template_name = "orders/cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["order"] = Order.objects.filter(customer_id=self.request.user.id, is_paid=False).last()
        return context
