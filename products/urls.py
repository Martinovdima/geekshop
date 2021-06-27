from django.urls import path

from products.views import ProductView

app_name = 'products'

urlpatterns = [
    path('', ProductView.as_view(), name='index'),
    path('<int:pk>/', ProductView.as_view(), name='product'),
    path('page/<int:page>/', ProductView.as_view(), name='page'),
]