from django.db import models
from product.models import Product
from authentication.models import Customer

# Create your models here.

class Order(models.Model):
    SHIPPING_FEE = 15

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=2, decimal_places=1, default=0)

    def calculate_total_order_price(self):
        total_price = 0
        for product_type in self.producttype_set.all():
            total_price += product_type.quantity * product_type.product.price

        return total_price

    def calculate_total_order_price_with_shipping_fee(self):
        return self.calculate_total_order_price() + + self.SHIPPING_FEE

class ProductType(models.Model):
    SIZE_CHOICES = [
        ("XS", "XS"),
        ("S", "S"),
        ("M", "M"),
        ("ML", "ML"),
        ("XL", "XL"),
    ]
    COLOR_CHOICES =[
        ("BLACK", "Black"),
        ("WHITE", "White"),
        ("RED", "Red"),
        ("BLUE", "Blue"),
        ("GREEN", "Green"),
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    size = models.CharField(
        choices=SIZE_CHOICES,
        default="M",
    )
    color = models.CharField(
        choices=COLOR_CHOICES,
        default="RED",
    )

    def calculate_total_price(self):
        return self.quantity * self.product.price
