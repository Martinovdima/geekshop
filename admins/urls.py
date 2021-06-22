from django.urls import path

from admins.views import UserListView, UserCreateView, UserUpdateView, UserDeleteView, index, \
    admin_products, admin_products_category, admin_products_category_create, admin_products_category_update, \
    admin_products_category_delete, admin_products_create, admin_products_delete, admin_products_update

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users/create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='admin_users_delete'),
    #path('users/return/<int:id>/', admin_users_return, name='admin_users_return'),
    path('products/', admin_products, name='admin_products'),
    path('products/create/', admin_products_create, name='admin_products_create'),
    path('products/delete/<int:id>/', admin_products_delete, name='admin_products_delete'),
    path('products/update/<int:id>/', admin_products_update, name='admin_products_update'),
    path('products-category/', admin_products_category, name='admin_products_category'),
    path('products-category/create/', admin_products_category_create, name='admin_products_category_create'),
    path('products-category/delete/<int:id>/', admin_products_category_delete, name='admin_products_category_delete'),
    path('products-category/update/<int:id>/', admin_products_category_update, name='admin_products_category_update'),

]