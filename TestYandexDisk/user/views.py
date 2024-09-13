from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from user.forms import UserLoginForm, UserRegisterForm, UserPasswordChangeForm


class LoginUser(LoginView):
    form_class = UserLoginForm
    template_name = 'login.html'
    extra_context = {'title': 'Авторизация'}


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('main'))


class RegisterUser(CreateView):
    form_class = UserRegisterForm
    template_name = 'register.html'
    extra_context = {'title': 'Регистрация'}
    success_url = reverse_lazy('login')


