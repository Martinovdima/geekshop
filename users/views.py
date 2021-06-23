from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView, UpdateView

from users.forms import UserLoginForm, UserRegisterForm
from admins.forms import UserAdminProfileForm
from basket.models import Basket
from users.models import User


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserLoginView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop - Админ | Авторизация'
        return context

class UserRegisterView(CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserRegisterView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop - Админ | Регистрация'
        return context

class UserProfileView(UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = UserAdminProfileForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop | Личный кабинет'
        context['basket'] = Basket.objects.filter(user=self.request.user)
        return context

class UserLogoutView(LogoutView):
    redirect_field_name = None

