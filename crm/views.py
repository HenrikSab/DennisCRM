from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return HttpResponse('home')

def customers(request):
    return render(request, 'crm/customers.html')
def products(request):
    return render(request, 'crm/products.html')
def dashboard(request):
    return render(request, 'crm/dashboard.html')

# Create your views here.
