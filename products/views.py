from django.shortcuts import render
import os
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

from products.models import ProductCategory, Product


MODULE_DIR = os.path.dirname(__file__)

def index(request):
    content = {'title': 'geekShop'}
    return render(request, 'products/index.html', content)

class ProductView(ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop | Продукты'
        context['category'] = ProductCategory.objects.all()
        return context

#def products(request, category_id=None, page=1):
    #content = {'categories': ProductCategory.objects.all(),'title': 'GeekShop - каталог',}
    #products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()

    #paginator = Paginator(products, 3)
    #try:
        #products_paginator = paginator.page(page)
    #except PageNotAnInteger:
        #products_paginator = paginator.page(1)
    #except EmptyPage:
        #products_paginator = paginator.page(paginator.num_pages)
    #content['products'] = products_paginator
    #return render(request, 'products/products.html', content)
