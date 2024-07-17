from django.shortcuts import get_object_or_404, render
from .models import Product, Customer

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    context ={
        'products': products,
    }
    return render(request,'Djangoapp/product_list.html', context)

def product_detail(request, pk):
    product = get_object_or_404(product, pk=pk)
    context ={
        'products': product,
    }
    return render(request, 'Djangoapp/product_details.html', context)

def customer_list(request):
    customers = Customer.objects.all()
    context ={
        'customers': customers
    }
    return render(request, 'Djangoapp/customer_list.html', context)

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    context = {
         'customer': customer
    }
    return render(request, 'Djangoapp/customer_detail.html', context)
 

from django.shortcuts import render

def home(request):
    context = {
        'message': 'Welcome to the Home Page!'
    }
    return render(request, 'Djangoapp/home.html', context)
