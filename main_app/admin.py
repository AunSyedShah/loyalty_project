from django.contrib import admin
from .models import Product, Category, UserCart, SubCategory
from django.contrib.sessions.models import Session

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(UserCart)
admin.site.register(Session)
admin.site.register(SubCategory)

