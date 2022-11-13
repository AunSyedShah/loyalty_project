from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/', views.add_product_cart, name='add_product_cart'),
    path('signup/', views.signup, name='signup'),
    path('checkout/', views.order_placed, name='checkout'),
    path('profile/', views.profile, name='profile'),
    path('order_placed/', views.order_placed, name='order_placed'),
    path('send_email/', views.send_email, name='send_email'),
]
