from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomerForm
from .models import Customer

# Create your views here.
from .models import Product
from .forms import CustomerForm

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')  # Redirect to a customer list or success page
    else:
        form = CustomerForm()
        
    return render(request, 'customers/add_customer.html', {'form': form})

def index(request):
     
    product_list = Product.objects.all() 
    return render(request, 'index.html', {'products': product_list})

def new(request):
    return HttpResponse('New Page')

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers/customer_list.html', {'customers': customers})


