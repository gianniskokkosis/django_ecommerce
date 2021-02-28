from django.contrib import admin
from .models import Invoice, Product, Wishlist

admin.site.register(Product)
admin.site.register(Invoice)
admin.site.register(Wishlist)
