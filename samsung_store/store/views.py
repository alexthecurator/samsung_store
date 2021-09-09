from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Phone, Store
from .forms import Purchase
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
    order = Purchase(request.POST)
    
    if request.method == 'POST':
        order = Purchase(request.POST)
        if order.is_valid():
            card = order.cleaned_data['card']
            csv= order.cleaned_data['csv']
            exp = order.cleaned_data['exp']
            email = order.cleaned_data['email']
            password = order.cleaned_data['password']

    else:
        error = "No post found"
        print(error)
        
    context = {
        'title':title,
        'phone':phone,
        'order':order,
    }
    
    return render(request, 'store/showcase.html', context)
