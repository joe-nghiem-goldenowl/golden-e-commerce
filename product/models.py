from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "category"


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    additional_description = models.TextField()
    additional_info = models.TextField()
    price = models.IntegerField(default=0)
    star = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    is_active = models.BooleanField(default=True)
    discount = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "product"


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_url = models.URLField(max_length=255)

    def __str__(self):
        return self.image_url

    class Meta:
        db_table = "image"
