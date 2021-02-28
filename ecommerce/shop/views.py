from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product, Invoice

def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }

    return render(request, 'shop/home.html', context)

def about(request):
    return render(request, 'shop/about.html')

def product_details(request, pk):
    obj = Product.objects.get(id=pk)
    context = {
        'obj': obj
    }

    return render(request, 'shop/product_details.html', context)
    
def checkout(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == "POST":
        name = request.POST.get('name', '')
        surnname = request.POST.get('surname', '')
        email = request.POST.get('email', '')
        iban = request.POST.get('iban', '')
        card_type = request.POST.get('card_type', '')
        name = request.POST.get('name', '')
        Invoice.objects.create(name=name, surname=surnname, email=email, iban=iban, card_type=card_type)
        return HttpResponseRedirect('/')
    
    context = {
        'obj': product
    }
    return render(request, 'shop/checkout.html', context)

        