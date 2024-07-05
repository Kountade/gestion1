from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Order
from django.contrib.auth.decorators import login_required
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

@login_required(login_url='user-login')
def index(request):
    products = Product.objects.all()
    product_count = Product.objects.all().count()
    orders = Order.objects.all()
    workers_count =  User.objects.all().count()
    order_count = Order.objects.all().count()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
             instance = form.save(commit=False)
             instance.staff = request.user
             instance.save()
             return redirect('dash-index')
    else:
       form = OrderForm()
    context = {
        'form': form,
        'orders': orders,
        'products': products,
        'product_count': product_count,
        'order_count': order_count,
        'workers_count': workers_count,
    }
  

    return render(request,'dash/index.html', context)


@login_required(login_url='user-login')
def staff(request):
    
    workers = User.objects.all()
    workers_count = workers.count()
    product_count =  Product.objects.all().count()
    order_count = Order.objects.all().count()
    context = {'workers': workers, 
               'workers_count':workers_count,
               'product_count':product_count, 
               'order_count':order_count}
    return render(request,'dash/staff.html',context)

def staff_detail(request, pk):
    workers = User.objects.get(id=pk)
    
    context = {'workers': workers,
             
               }
    
    return render(request,'dash/staff_detail.html',context)


@login_required(login_url='user-login')
def product(request):
    order_count = Order.objects.all().count()
    workers_count =  User.objects.all().count()
    product = Product.objects.all()
    product_count = product.count()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
          
           
            return redirect('dash-product')
    else:
        form = ProductForm()
    context = {
        'product': product,
        'form': form, 
        'workers_count': workers_count,
        'product_count': product_count,
        'order_count':order_count,
    }
    return render(request,'dash/product.html',context)
@login_required
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dash-product')
    context = {
        'item': item
    }
    return render(request, 'dash/product_delete.html', context)
@login_required
def product_edit(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dash-product')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dash/product_edit.html', context)





   

@login_required(login_url='user-login')
def profil(request):
    return render(request,'dash/profil.html')

@login_required
def order(request):
    product_count =  Product.objects.all().count()
    orders = Order.objects.all()
    order_count = orders.count()
    workers_count =  User.objects.all().count()

    context = {
        'orders': orders,
        'order_count':order_count,
        'product_count':product_count,
        'workers_count':workers_count
        
    }
    return render(request, 'dash/order.html', context)
