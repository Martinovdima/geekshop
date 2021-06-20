from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from users.models import User
from products.models import Product, ProductCategory
from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, ProductCategoryForm
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'admins/admin.html')

@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    content = {'title': 'Geekshop - Админ | Пользователи','users': User.objects.all()}
    return render(request, 'admins/admin-users-read.html', content)

@user_passes_test(lambda u: u.is_superuser)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegisterForm()
    content = {'title': 'Geekshop - Админ | Регистрация', 'form': form}
    return render(request, 'admins/admin-users-create.html', content)

@user_passes_test(lambda u: u.is_superuser)
def admin_users_update(request, id):
    selected_user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=selected_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=selected_user)

    content = {
        'title': 'Geekshop - Админ | Обновление пользователя',
        'form': form,
        'selected_user': selected_user,
    }
    return render(request, 'admins/admin-users-update-delete.html', content)

@user_passes_test(lambda u: u.is_superuser)
def admin_users_delete(request, id):
    user =User.objects.get(id=id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))


@user_passes_test(lambda u: u.is_superuser)
def admin_users_return(request, id):
    user = User.objects.get(id=id)
    user.is_active = True
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))


@user_passes_test(lambda u: u.is_superuser)
def admin_products(request):
    content = {'title': 'Geekshop - Админ | Продукты', 'products': Product.objects.all()}
    return render(request, 'admins/admin-products-read.html', content)

@user_passes_test(lambda u: u.is_superuser)
def admin_products_category(request):
    content = {'title': 'Geekshop - Админ | Категории','products_category': ProductCategory.objects.all()}
    return render(request, 'admins/admin-products-category-read.html', content)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_category_create(request):
    if request.method == 'POST':
        form = ProductCategoryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_products_category'))
    else:
        form = ProductCategoryForm()
    content = {'title': 'Geekshop - Админ | Создание категории', 'form': form}
    return render(request, 'admins/admin-products-category-create.html', content)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_category_update(request, id):
    selected_products_category = ProductCategory.objects.get(id=id)
    if request.method == 'POST':
        form = ProductCategoryForm(data=request.POST, instance=selected_products_category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_products_category'))
    else:
        form = ProductCategoryForm(instance=selected_products_category)

    content = {
        'title': 'Geekshop - Админ | Обновление категории',
        'form': form,
        'selected_products_category': selected_products_category,
    }
    return render(request, 'admins/admin-products-category-update-delete.html', content)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_category_delete(request, id):
    product_category =ProductCategory.objects.get(id=id)
    product_category.delete()
    return HttpResponseRedirect(reverse('admins:admin_products_category'))