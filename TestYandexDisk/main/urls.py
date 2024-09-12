from django.urls import path
import main.views as main

urlpatterns = [
    path('', main.MainTemplateView.as_view(), name='main'),
    path('disk/', main.DiskTemplateView.as_view(), name='disk'),
    path('download/', main.DownloadTemplateView.as_view(), name='download'),
]
