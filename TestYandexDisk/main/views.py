import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from typing import List, Dict, Any


def get_files_list(public_key: str) -> List[Dict[str, Any]]:
    """Получает список файлов и папок с Яндекс.Диска по публичной ссылке.
    Args:
        public_key (str): Публичная ссылка на Яндекс.Диск.
    Returns:
        List[Dict[str, Any]]: Список файлов и папок в виде словаря.
            Если ссылка неверна или доступ запрещен, возвращает пустой список."""

    url = f'https://cloud-api.yandex.net/v1/disk/public/resources?public_key={public_key}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('_embedded').get('items')
    return []


def download_files_disk(public_key: str) -> str:
    """Получает ссылку для скачивания файла или папки с Яндекс.Диска по публичной ссылке.
    Args:
        public_key (str): Публичная ссылка на Яндекс.Диск.
    Returns:
        str: Ссылка для скачивания.
            Если ссылка неверна или доступ запрещен, возвращает пустую строку."""

    url = f'https://cloud-api.yandex.net/v1/disk/public/resources/download?public_key={public_key}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('href')
    return ''


class MainTemplateView(TemplateView):
    """ Представление для отображения главной страницы."""

    template_name = 'main.html'


class DiskTemplateView(LoginRequiredMixin, TemplateView):
    """ Представление для отображения списка файлов с Яндекс.Диска.
    Требует авторизации пользователя.
    Returns:
        dict: Контекстные данные для шаблона."""

    template_name = 'yandex_disk.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        public_key = self.request.GET.get('public_key')
        files = get_files_list(public_key) if public_key else []
        context['title'] = 'Приложения для просмотра файлов с Яндекс.Диск'
        context['files'] = files
        context['public_key'] = public_key
        return context


class DownloadTemplateView(TemplateView):
    """ Представление для отображения ссылки для скачивания файла или папки с Яндекс.Диска.
    Требует авторизации пользователя.
    Returns:
        dict: Контекстные данные для шаблона."""

    template_name = 'yandex_disk.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        public_key = self.request.GET.get('download')
        print(f'{public_key} - download')
        download_link = download_files_disk(public_key) if public_key else ''
        context['link'] = download_link

        return context







