from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-input-auth',
                                                             'placeholder': 'Введите логин или E-mail'}))
    password = forms.CharField(max_length=50,
                               widget=forms.PasswordInput(attrs={'class': 'form-input-auth',
                                                                 'placeholder': 'Введите пароль'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-input-reg', 'placeholder': 'Логин'}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-input-reg', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Повтор пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-input-reg', 'placeholder': 'Повторите пароль'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'email': 'E-mail',
        }
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-input-reg', 'placeholder': 'E-mail'}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password1']

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с данным email уже зарегистрирован.')
        return email


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Текущий пароль',
                                   widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password1 = forms.CharField(label='Новый пароль',
                                    widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password2 = forms.CharField(label='Подтвердите новый пароль',
                                    widget=forms.PasswordInput(attrs={'class': 'form-input'}))

