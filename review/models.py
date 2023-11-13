from django.db import models

from product.models import Product


# Create your models here.
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.TextField()

    class Meta:
        db_table = "review"
