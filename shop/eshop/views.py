import json
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.serializers import serialize
from .models import User, Product, Availability, Size, Cart
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return render(request, "eshop/index.html")


def load_products(request):
    products = Product.objects.all()

    return JsonResponse({
        "products": [product.serialize() for product in products]})

def load_product_page(request, product_id):
    available_sizes =[]
    product = Product.objects.get(pk=product_id)
    availability = Availability.objects.filter(product = product)
    for available in availability:
        available_sizes.append(available.size.eu)
    sizes = Size.objects.all().order_by('eu')


    print(available_sizes)
    return render(request, "eshop/product_page.html",{
        "product" : product.serialize(),
       "available_sizes": available_sizes,
       "sizes": sizes
    })

def get_count_of_cart(request):
    count_of_cart = Cart.objects.filter(user = request.user).count()
    print(count_of_cart)
    return JsonResponse({"count_of_cart": count_of_cart})


@csrf_exempt
def cart(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    if request.method == "GET":
        cart_products = Cart.objects.filter(user = request.user)
        return render(request, "eshop/cart.html", {
            "cart_products" : cart_products
        })


    product_info = json.loads(request.body)
    product_code = product_info.get('product_code')
    size = product_info.get('size')
    product = Product.objects.get(product_code=product_code)
    size = Size.objects.get(eu=size)

    if request.method == 'POST':
        update_cart = Cart(
            user = request.user,
            product = product,
            size = size
        )
        update_cart.save()
        return JsonResponse({"succes": "added product to cart"})

    if request.method =="DELETE":
        product = Cart.objects.get(
            user = request.user, 
            product = product, 
            size = size)
        product.delete()

        return JsonResponse({"succes":"Delete product from cart"})


def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else: 
            return render(request,"eshop/login.html",{
                "message" : "Invalid username and/or password"
            })

    return render(request, "eshop/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "eshop/register.html",{
                "message" : "Passwords do not match"
            })
        
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "eshop/register.html",{
                "message": "Username already taken"
            })
        login(request,user)
        return HttpResponseRedirect(reverse("index"))

    return render(request, "eshop/register.html")