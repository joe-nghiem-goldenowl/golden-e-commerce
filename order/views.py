from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from rest_framework import status

from .models import Order


# Create your views here.
class CartView(TemplateView):
    model = Order
    template_name = "orders/cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["order"] = Order.objects.filter(
            customer_id=self.request.user.id, is_paid=False
        ).last()
        return context


def add_to_cart(request):
    product_id = request.GET.get("product_id")
    product_quantity = request.GET.get("product_quantity")
    product_color = request.GET.get("product_color")
    product_size = request.GET.get("product_size")

    try:
        order, _ = Order.objects.get_or_create(
            customer_id=request.user.id, is_paid=False
        )

        order.producttype_set.create(
            product_id=product_id,
            quantity=product_quantity,
            size=product_size,
            color=product_color,
        )

        return JsonResponse({"message": "success"}, status=status.HTTP_200_OK)
    except (ValueError, TypeError, IntegrityError):
        import traceback

        traceback.print_exc()
        return JsonResponse(
            {"message": "error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
