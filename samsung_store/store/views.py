from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Phone, Store
# Create your views here.

def home_view(request):
    title = "Home"
    context = {
        'title':title,
    }
    return render(request, 'home.html', context)

def product_view(request):
    qs = Phone.objects.all()
    return render(request, 'home.html', {'qs':qs})