from django.contrib import admin
from .models import User, Product, Availability, Size, Cart

# Register your models here.

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Availability)
admin.site.register(Size)
admin.site.register(Cart)