'''
Some various imports. More specifically python libraries and some models from the database
'''
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product, Invoice, Wishlist

def home(request):
    '''
    Home view gets all the products from the database with products = Product.objects.all()
    command, stores them in a python dictionary called context and then renders the context 
    to the home.html page where all the products are printed out one by one.
    '''
    products = Product.objects.all()
    context = {
        'products': products
    }

    return render(request, 'shop/home.html', context)

def about(request):
    '''
    About view just renders the about.html page. 
    '''
    return render(request, 'shop/about.html')

def product_details(request, pk):
    '''
    Product details view retrieves a specific product from the database,
    stores it in a python dictionary called context and then renders the
    context to the product_details.html where the details of a product 
    are printed out
    '''
    obj = Product.objects.get(id=pk)
    context = {
        'obj': obj
    }

    return render(request, 'shop/product_details.html', context)
    
def checkout(request, pk):
    '''
    Checkout view takes all the form's parameters from the request
    and then creates a new Invoice(a new Purchase) to the database(Invoice table)
    '''
    product = Product.objects.get(id=pk)
    if request.method == "POST":
        name = request.POST.get('name', '')
        surnname = request.POST.get('surname', '')
        email = request.POST.get('email', '')
        iban = request.POST.get('iban', '')
        card_type = request.POST.get('card_type', '')
        Invoice.objects.create(name=name, surname=surnname, email=email, iban=iban, card_type=card_type, product=product)
        return HttpResponseRedirect('/')
    
    context = {
        'obj': product
    }
    return render(request, 'shop/checkout.html', context)

def my_wishlist(request):
    '''
    My Wishlist view takes all the wishlist items from the database,
    stores them in a python dictionary called context and then renders
    context to the wishlist.html where all the wishlist items are printed out
    one by one
    '''
    wishlist = Wishlist.objects.all()
    context = {
        "wishlist": wishlist
    }
    return render(request, 'shop/wishlist.html', context)  


def add_to_wishlist(request, pk):
    '''
    Add to wishlist view takes a specific product from the database that the user 
    wants to put in his/her wishlist and then creates a new item in the Wishlist table
    '''
    product = Product.objects.get(id=pk)
    Wishlist.objects.create(product=product)
    return HttpResponseRedirect('/') 

def delete_from_wishlist(request, pk):
    '''
    Delete from wishlist view finds a specific product in the Wishlist table
    and when it finds the product that the user wants to delete from the his/her
    wishlist, it hust deleted it from the database
    '''
    Wishlist.objects.get(product__id=pk).delete()
    return HttpResponseRedirect('/')     