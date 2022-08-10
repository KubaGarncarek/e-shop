from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

    def __str__(self):
        return self.username
    
class Product(models.Model):
    name = models.CharField(max_length=64)
    product_code = models.CharField(max_length=16)
    price = models.IntegerField(null=False)
    photo = models.CharField(max_length=128)
    category = models.CharField(max_length=16)

    def serialize(self):
        return {
            "id": self.id,
            "name" : self.name,
            "product_code" : self.product_code,
            "price" : self.price,
            "photo" : self.photo,
            "category" : self.category
        }

    def __str__(self):
        return self.product_code
    
class Availability(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    size = models.ForeignKey("Size", on_delete=models.CASCADE)
    count_of_size = models.IntegerField(default=0)
    


    def serialize(self):
        return { 
            "product_code" : self.product.product_code,
            "size" : self.size.eu,
            "count_of_size" : self.count_of_size
        }
    def __tuple__(self):
        return (
            self.product,
            self.size,
            self.count_of_size         
        )




class Size(models.Model):
    eu = models.IntegerField()

    def __str__(self):
        return str(self.eu)