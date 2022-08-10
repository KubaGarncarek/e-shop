from itertools import product
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core.serializers import serialize
from .models import User, Product, Availability, Size
from django.forms.models import model_to_dict

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