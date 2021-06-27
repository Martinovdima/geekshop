from django.urls import path

from admins.views import UserListView, UserCreateView, UserUpdateView, UserDeleteView, UserReturnView, index, \
    ProductListView, ProductCategoryListView, ProductCategoryCreateView, ProductCategoryUpdateView, \
    ProductCategoryDeleteView, ProductCreateView, ProductDeleteView, ProductUpdateView

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users/create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='admin_users_delete'),
    path('users/return/<int:pk>/', UserReturnView.as_view(), name='admin_users_return'),
    path('products/', ProductListView.as_view(), name='admin_products'),
    path('products/create/', ProductCreateView.as_view(), name='admin_products_create'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='admin_products_delete'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='admin_products_update'),
    path('products-category/', ProductCategoryListView.as_view(), name='admin_products_category'),
    path('products-category/create/', ProductCategoryCreateView.as_view(), name='admin_products_category_create'),
    path('products-category/delete/<int:pk>/', ProductCategoryDeleteView.as_view(), name='admin_products_category_delete'),
    path('products-category/update/<int:pk>/', ProductCategoryUpdateView.as_view(), name='admin_products_category_update'),

]