from itertools import product
from .models import product
from .forms import Productform
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    if request.method == 'POST':
        fm = Productform(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('home')  # Redirect to refresh the page
    else:
        fm = Productform()

    prod = product.objects.all()
    fm = Productform()
    return render(request, 'Electronics/home.html',{"prod":prod,'fm':fm})

def edit_product(request, product_id):
    prod = product.objects.get(id=product_id)
    if request.method == 'POST':
        fm = Productform(request.POST, instance=prod)
        if fm.is_valid():
            fm.save()
            return redirect('home')  # Redirect to refresh the page
    else:
        fm = Productform(instance=prod)

    return render(request, 'Electronics/edit_product.html', {'fm': fm})

def delete_product(request, product_id):
    prod = product.objects.get(id=product_id)
    if request.method == 'POST':
        prod.delete()
        return redirect('home')  # Redirect to refresh the page
    return render(request, 'Electronics/delete_product.html', {'prod': prod})