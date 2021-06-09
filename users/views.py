from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse

from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from basket.models import Basket


# Create your views here.

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    content= {'title': 'Geekshop - Авторизация', 'form': form}

    return render(request, 'users/login.html', content)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegisterForm()
    content = {'title': 'Geekshop - Регистрация', 'form': form}

    return render(request, 'users/register.html', content)

def profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Успешно сохранено!')
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=user)
    content = {
        'title': 'Geekshop - Личный кабинет',
        'form': form,
        'basket': Basket.objects.filter(user=user),
    }
    return render(request, 'users/profile.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
