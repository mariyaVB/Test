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

    def get_success_url(self):
        return reverse_lazy('main')


class LogoutUser(LogoutView):
    next_page = reverse_lazy('main')


class RegisterUser(CreateView):
    form_class = UserRegisterForm
    template_name = 'register.html'
    extra_context = {'title': 'Регистрация'}
    success_url = reverse_lazy('login')


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy('password_change_done')
    template_name = 'password_change_form.html'
    title = 'Смена пароля'
    extra_context = {'title': 'Изменение пароля'}
