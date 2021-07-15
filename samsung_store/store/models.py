from django.db import models
from .utils import unique_id

# Create your models here.
class Phone(models.Model):
    identity = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    about = models.TextFiled(max_length=250)
    image = models.FileField(_("image"), upload_to='assets/phones', max_length=100)
    rating = models.IntegerField(max_length=5)
    price = models.FloatField(max_length=255, blank=True)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Name: {self.name}, Ratings: {self.rating} stars, Price: {self.price}$"
        

class Store(models.Model):
    sale_id = models.CharField(max_length=150)
    name = models.CharFiled(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Store: {self.name}, Date: {self.date}"