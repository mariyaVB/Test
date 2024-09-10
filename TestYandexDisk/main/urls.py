from django.urls import path
import main.views as main

urlpatterns = [
    path('', main.MainTemplateView.as_view(), name='main'),
]
