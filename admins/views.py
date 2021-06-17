from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from users.models import User
from admins.forms import UserAdminRegisterForm


def index(request):
    return render(request, 'admins/admin.html')

def admin_users(request):
    content = {'title': 'Geekshop - Админ | Пользователи','users': User.objects.all()}
    return render(request, 'admins/admin-users-read.html', content)

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

def admin_users_update(request, id):
    return render(request, 'admins/admin-users-update-delete.html')

def admin_users_delete(request, id):
    pass
