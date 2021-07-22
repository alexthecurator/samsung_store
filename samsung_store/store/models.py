from django.db import models
from .utils import unique_id
from django.utils import timezone

# Create your models here.
class Phone(models.Model):
    # store = models.ForeignKey('store.Store', on_delete=models.CASCADE, blank=unique_id())
    name = models.CharField(max_length=100)
    about = models.TextField(max_length=250)
    image = models.FileField(upload_to='samsung_store/assets/phones', max_length=100)
    rating = models.IntegerField(blank=True)
    price = models.FloatField(max_length=255, blank=True)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Name: {self.name},  Ratings: {self.rating} stars,  Price: {self.price}$"
        
class Store(models.Model):
    thestore_id = models.CharField(max_length=150, blank=True)
    name = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if self.thestore_id == "":
            self.thestore_id = unique_id()
        if self.date == "":
            self.date = timezone.now()
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Store: {self.name},  Date: {self.date}"    
class Buyers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()