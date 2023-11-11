from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
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
    name = models.CharField(max_length=255)
    description = models.TextField()
    additional_description = models.TextField()
    additional_info = models.TextField()
    price = models.IntegerField(default=0)
    size = models.CharField(
        choices=SIZE_CHOICES,
        default="M",
    )
    color = models.CharField(
        choices=COLOR_CHOICES,
        default="RED",
    )
    is_active = models.BooleanField(default=True)
    discount = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_url = models.URLField(max_length=255)

    def __str__(self):
        return self.image_url
