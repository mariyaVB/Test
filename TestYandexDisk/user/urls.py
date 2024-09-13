from django.contrib.auth.views import LogoutView
from django.urls import path
import user.views as user

urlpatterns = [
    path('login/', user.LoginUser.as_view(), name='login'),
    path('logout/', user.logout_user, name='logout'),
    path('register/', user.RegisterUser.as_view(), name='register'),
]
