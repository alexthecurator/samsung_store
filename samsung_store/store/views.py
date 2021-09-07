from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Phone, Store
from .forms import Purchasing
from globalpayments.api import ServicesConfig, ServicesContainer
# Create your views here.

def home_view(request):
    title = "Home"
    context = {
        'title':title,
    }
    return render(request, 'store/home.html', context)

def showcase_view(request):
    title = "Showcase"
    phone = Phone.objects.all()
    
    if request.method == 'POST':
        form = Purchasing(request.POST)
        if form.is_valid():
            pass
        
    context = {
        'title':title,
        'phone':phone,
    }
    return render(request, 'store/showcase.html', context)