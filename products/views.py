from django.shortcuts import render
import os
import json
from products.models import ProductCategory, Product



MODULE_DIR = os.path.dirname(__file__)
# Create your views here.

def index(request):
    content = {'title': 'geekShop'}
    return render(request, 'products/index.html', content)


def products(request):
    links_menu = ProductCategory.objects.all()
    products = Product.objects.all()

    content = {
        'links_menu': links_menu,
        'title': 'geekShop - каталог',
        'products': products,
    }

    return render(request, 'products/products.html', content)
