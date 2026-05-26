from django.shortcuts import get_object_or_404, redirect, render
from django.template.context_processors import request
from .models import Product
from .forms import ProductForm

# Create your views here.

# CRUD = create, read, update, delete

# Home View
def home_view(request):
    return render(request, 'imsApp/home.html')

# Create View
def product_create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'imsApp/product_form.html', {'form':form})
        
# Read View
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'imsApp/product_list.html', {'products':products})

# Update View
def product_update_view(request,product_id):
    product = Product.objects.get(product_id=product_id)
    form = ProductForm()
    if request.method == 'POST' :
        ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        return render(request, 'imsApp/product_form.html', {'form':form})
    
# Delete View
def product_del_view(request,product_id):
    product = Product.objects.get(product_id=product_id)
    context = {'product':product}
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request,'imsApp/prod_confirm_del.html',context)