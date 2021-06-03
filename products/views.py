from django.shortcuts import render


# Create your views here.

def index(request):
    content = {
        'title': 'geekShop',
    }
    return render(request, 'products/index.html', content)


def products(request):
    links_menu = [
        {'href': 'products', 'name': 'новинки'},
        {'href': 'products', 'name': 'одежда'},
        {'href': 'products', 'name': 'обувь'},
        {'href': 'products', 'name': 'аксессуары'},
        {'href': 'products', 'name': 'подарки'},
    ]
    products = [
        {'name': 'худи черного цвета с монограммами adidas Originals',
         'price': '6 090,00',
         'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
         'image': 'vendor/img/products/Adidas-hoodie.png'
         },
        {'name': 'синяя куртка The North Face',
         'price': '23 725,00',
         'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
         'image': 'vendor/img/products/Blue-jacket-The-North-Face.png'
         },
        {'name': 'коричневый спортивный oversized-топ ASOS DESIGN',
         'price': '3 390,00',
         'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
         'image': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'
         },
        {'name': 'черный рюкзак Nike Heritage',
         'price': '2 340,00',
         'description': 'Плотная ткань. Легкий материал.',
         'image': 'vendor/img/products/Black-Nike-Heritage-backpack.png'
         },
        {'name': 'черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
         'price': '13 590,00',
         'description': 'Гладкий кожаный верх. Натуральный материал.',
         'image': 'vendor/img/products/Black-Dr-Martens-shoes.png'
         },
        {'name': 'чемно-синие широкие строгие брюки ASOS DESIGN',
         'price': '2890,00',
         'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
         'image': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'
         },

    ]
    content = {
        'date': '2020',
        'products': products,
        'links_menu': links_menu,
        'title': 'geekShop - каталог',
    }
    return render(request, 'products/products.html', content)
