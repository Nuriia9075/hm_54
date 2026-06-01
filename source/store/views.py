from django.shortcuts import render

from store.models import Product

# Create your views here.
def products(request):
    products = Product.objects.all()

def add_product(request):
    pass

def product_detail(request):
    pass
def product_edit(request):
    pass

def categories(request):
    pass
def add_category(request):
    pass
def category_detail(request):
    pass
def category_edit(request):
    pass