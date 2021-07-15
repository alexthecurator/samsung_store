from django.db import models
from .utils import unique_id
from django.utils import timezone

# Create your models here.
class Phone(models.Model):
    # from_store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    about = models.TextField(max_length=250)
    image = models.FileField(upload_to='assets/phones', max_length=100)
    rating = models.IntegerField(blank=True)
    price = models.FloatField(max_length=255, blank=True)
    store = models.ForeignKey('store.Store', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Name: {self.name}, Ratings: {self.rating} stars, Price: {self.price}$"
        

class Store(models.Model):
    sale_id = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Store: {self.name}, Date: {self.date}"
    
    def save(self, *args, **kwargs):
        if self.sales_id == "":
            self.sales_id = unique_id()
        if self.date == "":
            self.date = timezone.now() ## Adds the current timestap
        return super().save(*args, **kwargs)
        
class Buyers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()