from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100, default='')
    product_price = models.FloatField(default=0)
    loyalty_points = models.IntegerField(default=0)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='product_images', default='')

    def __str__(self):
        return self.product_name


class UserCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, default='')
    loyalty_points = models.IntegerField(default=0)
    products = models.ManyToManyField(Product, blank=True)
