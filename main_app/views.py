from django.shortcuts import render, redirect
from .models import Product, Category, UserCart
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
import json
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from cart.cart import Cart


# Create your views here.
def home(request):
    context = {}
    if request.method == "POST":
        if "category_button" in request.POST:
            selected_category = request.POST.get('selected_category')
            products = Product.objects.filter(product_category=selected_category)
            context['products'] = products
            context['categories'] = Category.objects.all()
            return render(request, 'home.html', context)
    context['products'] = Product.objects.all()
    context['categories'] = Category.objects.all()
    return render(request, 'home.html', context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            # initialize user cart
            if not UserCart.objects.filter(user=user).exists():
                UserCart.objects.create(user=user)
            return redirect('main_app:home')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect(request.path)
    else:
        return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('main_app:home')


def cart(request):
    context = {}
    if request.user.is_authenticated:
        user_cart = UserCart.objects.get(user=request.user)
        cart_items = user_cart.products.all()
        grand_total = 0
        for item in cart_items:
            grand_total += item.product_price
        total_loyalty_points = 0
        for item in cart_items:
            total_loyalty_points += item.loyalty_points
        previous_loyalty_points = user_cart.loyalty_points
        # 10% of previous loyalty points
        discount = (previous_loyalty_points * 10) / 100
        context['discount'] = discount
        context['pre_loyalty_points'] = previous_loyalty_points
        context['loyalty_points'] = total_loyalty_points
        context['grand_total'] = grand_total
        context['cart_items'] = cart_items
        return render(request, 'cart.html', context)
    else:
        return redirect("login")


def add_product_cart(request):
    if request.method == 'POST':
        request_body = json.loads(request.body)
        product_id = request_body['product_id']
        product = Product.objects.get(id=product_id)
        user_cart = UserCart.objects.get(user=request.user)
        user_cart.products.add(product)
        user_cart.save()
        return JsonResponse({'success': True}, status=200)


def signup(request):
    context = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('home')
        else:
            messages.add_message(request, messages.ERROR, form.errors)
    registration_form = RegistrationForm()
    context['registration_form'] = registration_form
    return render(request, 'registration.html', context)


def order_placed(request):
    if request.method == 'POST':
        user_cart = UserCart.objects.get(user=request.user)
        products = user_cart.products.all()
        user_cart.loyalty_points = 0
        # add loyalty points to user_cart
        total_loyalty_points = 0
        for item in products:
            total_loyalty_points += item.loyalty_points
        user_cart.loyalty_points += total_loyalty_points
        user_cart.products.clear()
        user_cart.save()
        messages.success(request, 'Order placed successfully')
        return redirect('order_placed')
    return render(request, 'order_placed.html')


def profile(request):
    context = {}
    if request.user.is_authenticated:
        if request.method == "POST":
            if "address_btn" in request.POST:
                address = request.POST.get('address')
                user_cart = UserCart.objects.get(user=request.user)
                user_cart.address = address
                user_cart.save()
                messages.success(request, 'Address updated successfully')
                return redirect(request.path)
        user_cart = UserCart.objects.get(user=request.user)
        context['user_cart'] = user_cart
        return render(request, 'profile.html', context)
    else:
        return redirect("login")


def send_email(request):
    send_mail("testing", "testing", settings.EMAIL_HOST_USER, ['aunsyedshah.drama@gmail.com'])
    return JsonResponse({'success': True}, status=200)


@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    messages.success(request, 'Product added to cart successfully')
    return redirect("main_app:home")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("main_app:cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("main_app:cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("main_app:cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("main_app:cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    # if cart_total does not exist in session
    if 'cart_total' not in request.session:
        request.session['cart_total'] = 0
    # if total_loyalty_points does not exist in session
    if 'total_loyalty_points' not in request.session:
        request.session['total_loyalty_points'] = 0
    return render(request, 'cart/cart_detail.html')
