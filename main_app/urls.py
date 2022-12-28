from django.urls import path
from . import views

app_name = 'main_app'

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
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_cl ear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail, name='cart_detail'),
]
