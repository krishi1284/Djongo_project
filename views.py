from django.shortcuts import render, redirect, get_object_or_404
from .models import Product


# Create your views here.


def product_list(request):
    product = Product.objects.all()
    return render(request, 'Cust.html', {'product': product})
   

def product_create(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        product_price = request.POST['product_price']
        quantity = request.POST['quantity']
        Product.objects.create(product_name=product_name, product_price=product_price, quantity=quantity)
        return redirect('product_list')
    return render(request, 'product_form.html',{'product': None})

def product_update(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        product.product_name = request.POST['product_name']
        product.product_price = request.POST['product_price']
        product.quantity = request.POST['quantity']
        product.save()
        return redirect('product_list')
    return render(request, 'product_form.html', {'product': product})

def product_delete(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect('product_list')

   
