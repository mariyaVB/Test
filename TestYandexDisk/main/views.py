from django.views.generic import TemplateView


class MainTemplateView(TemplateView):
    template_name = 'main.html'
    extra_context = {
        'title': 'Приложения для просмотра файлов с Яндекс.Диск',
    }
