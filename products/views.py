from django.shortcuts import render
import os
import json
from products.models import ProductCategory, Product



MODULE_DIR = os.path.dirname(__file__)
# Create your views here.

def index(request):
    content = {'title': 'geekShop'}
    return render(request, 'products/index.html', content)


def products(request, category_id=None):
    content = {
        'categories': ProductCategory.objects.all(),
        'title': 'GeekShop - каталог',
    }
    content.update({
        'products': Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    })
    return render(request, 'products/products.html', content)
