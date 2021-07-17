from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Phone, Store
# Create your views here.

def home_view(request):
    title = "Home"
    context = {
        'title':title,
    }
    return render(request, 'store/home.html', context)
