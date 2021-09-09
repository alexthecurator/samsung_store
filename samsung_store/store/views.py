from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseNotFound
from .models import Phone, Store
from .forms import Purchase
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def home_view(request):
    title = "Home"
    context = {
        'title':title,
    }
    return render(request, 'store/home.html', context)

def showcase_view(request):
    title = "Showcase"
    phone = Phone.objects.all()
    order = Purchase
    def order_checkout(self, *args, **kwargs):
        product_id = self.kwargs["phone_id"]
        product = Phone.objects.get(id=product_id)
        print(product)
        if request.method == 'POST':
            order = Purchase(request.POST) 
            if order.is_valid():
                card = order.cleaned_data['card']
                csv= order.cleaned_data['csv']
                exp = order.cleaned_data['exp']
                email = order.cleaned_data['email']
                password = order.cleaned_data['password']

                checkout_session = stripe.checkout.Session.create(
                    line_items=[
                        {
                            # TODO: replace this with the `price` of the product you want to sell
                            'name': phone.name,
                            'price': phone.price,
                            'quantity': 1,
                        },
                    ],
                    payment_method_types=[
                        'card',
                    ],
                    mode='payment',
                    success_url='store/showcase.html',
                    cancel_url='store/home.html',
                )
                
        else:
            error = "No post found"
            print(error)
            
    context = {
        'title':title,
        'phone':phone,
        'order':order,
    }
    
    return render(request, 'store/showcase.html', context)
