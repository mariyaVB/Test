from django.contrib.auth.views import PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path
import user.views as user

urlpatterns = [
    path('login/', user.LoginUser.as_view(), name='login'),
    path('logout/', user.LogoutUser.as_view(), name='logout'),
    path('register/', user.RegisterUser.as_view(), name='register'),
]
