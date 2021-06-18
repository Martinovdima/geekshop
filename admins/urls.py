from django.urls import path

from admins.views import admin_users, admin_users_create, admin_users_update, admin_users_delete, index, admin_users_return, admin_products, admin_products_category

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
    path('users/create/', admin_users_create, name='admin_users_create'),
    path('users/update/<int:id>/', admin_users_update, name='admin_users_update'),
    path('users/delete/<int:id>/', admin_users_delete, name='admin_users_delete'),
    path('users/return/<int:id>/', admin_users_return, name='admin_users_return'),
    path('products/',admin_products, name='admin_products'),
    path('products-category/', admin_products_category, name='admin_products_category'),

]