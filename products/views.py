from django.shortcuts import render
import os
import json



MODULE_DIR = os.path.dirname(__file__)
# Create your views here.

def index(request):
    content = {'title': 'geekShop'}
    return render(request, 'products/index.html', content)


def products(request):
    links_menu = [
        {'href': 'products', 'name': 'новинки'},
        {'href': 'products', 'name': 'одежда'},
        {'href': 'products', 'name': 'обувь'},
        {'href': 'products', 'name': 'аксессуары'},
        {'href': 'products', 'name': 'подарки'},
    ]
    content = {
        'date': '2020',
        'links_menu': links_menu,
        'title': 'geekShop - каталог',
    }
    file_path = os.path.join(MODULE_DIR, 'fixtures/goods.json')
    content['products'] = json.load(open(file_path, encoding='utf-8'))

    return render(request, 'products/products.html', content)
