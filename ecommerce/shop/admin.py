from django.contrib import admin
from .models import Invoice, Product, Cart

admin.site.register(Product)
admin.site.register(Invoice)
admin.site.register(Cart)
