from django.urls import path

from .views import *

urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path("products/", ProductListView.as_view(), name="products"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
]
