from django.contrib import admin
from .models import User, Product, Availability, Size

# Register your models here.

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Availability)
admin.site.register(Size)