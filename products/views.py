from django.shortcuts import render


# Create your views here.

def index(request):
    content = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', content)


def products(request):
    content = {
        'title': 'GeekShop - Каталог',
    }
    return render(request, 'products/products.html', content)
