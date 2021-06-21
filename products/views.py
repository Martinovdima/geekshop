from django.shortcuts import render
import os
from products.models import ProductCategory, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


MODULE_DIR = os.path.dirname(__file__)
# Create your views here.

def index(request):
    content = {'title': 'geekShop'}
    return render(request, 'products/index.html', content)


def products(request, category_id=None, page=1):
    content = {'categories': ProductCategory.objects.all(),'title': 'GeekShop - каталог',}
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()

    paginator = Paginator(products, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    content['products'] = products_paginator
    return render(request, 'products/products.html', content)
