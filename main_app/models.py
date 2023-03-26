from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='', null=True, blank=True)

    def __str__(self):
        return self.name


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, default='')
    price = models.IntegerField(default=0)
    loyalty_points = models.IntegerField(default=0)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, default='', null=True, blank=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, default='', null=True, blank=True)
    image = models.ImageField(upload_to='products/', default='')

    def __str__(self):
        return self.name


class UserCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, default='')
    loyalty_points = models.IntegerField(default=0)
    loyalty_points_expiry_date = models.DateField(null=True, blank=True)
    products = models.ManyToManyField(Product, blank=True)
