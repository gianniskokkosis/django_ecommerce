from django.contrib import admin
from .models import Invoice, Product

admin.site.register(Product)
admin.site.register(Invoice)
