from django.shortcuts import redirect, render
from django.template.context_processors import request
from .models import Product
from .forms import ProductForm

# Create your views here.

#CRUD = create, read, update, delete

#Home View
def home_view(request):
    return render(request, 'imsApp/home.html')

#Create View
def product_create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'imsApp/product_form.html', {'form':form})
        
#Read View
def product_list_view(request):
    products = Product.all()
    return render(request, 'imsApp/product_list.html', {'products':products})

#Update View

#Delete View