from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, default='')
    price = models.IntegerField(default=0)
    loyalty_points = models.IntegerField(default=0)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', default='')

    def __str__(self):
        return self.name


class UserCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, default='')
    loyalty_points = models.IntegerField(default=0)
    products = models.ManyToManyField(Product, blank=True)
