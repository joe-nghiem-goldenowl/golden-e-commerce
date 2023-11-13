from django.urls import path
from .views import *

urlpatterns = [
  path("", CartView.as_view(), name="cart"),
  path("add-to-cart/", add_to_cart, name="add-to-cart"),

]
