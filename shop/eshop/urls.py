from django.urls import path 

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("registers", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout_view", views.logout_view, name="logout"),

    path("load_products", views.load_products, name="load_products"),
    path("load_product_page/<int:product_id>", views.load_product_page, name="load_product_page"),
]