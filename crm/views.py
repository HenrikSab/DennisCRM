from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm




def home(request):

    customers = Customer.objects.all()
    orders = Order.objects.all()

    total_orders = orders.count()
    order_dilevered = orders.filter(Status='Delivered').count()
    order_pending = orders.filter(Status='Pending').count()

    context = {'customers':customers, 'orders':orders, 'total_orders': total_orders, 'order_dilevered': order_dilevered, 'order_pending':order_pending }

    return render(request, 'crm/dashboard.html', context)

def customers(request, pk):
    customer = Customer.objects.get(id=pk)

    orders = customer.order_set.all()
    orders_count = orders.count()

    context = {'customer': customer, 'orders': orders, 'orders_count':orders_count}

    return render(request, 'crm/customers.html',context)

def products(request):
    products = Product.objects.all()
    return render(request, 'crm/products.html', {'products':products}   )

def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'crm/order_form.html', context )

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance = order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance = order )
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'form': form}
    return render(request, 'crm/order_form.html', context )


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method=='POST':
        order.delete()
        return redirect('/')

    context = {'item':order}
    return render(request, 'crm/delete.html', context)












# Create your views here.
