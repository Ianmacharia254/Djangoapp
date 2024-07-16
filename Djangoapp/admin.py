from django.contrib import admin
from .models import customer, product

# Register your models here.
admin.site.register(product)
admin.site.register(customer)