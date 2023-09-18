from django.shortcuts import get_object_or_404, render

from ice_cream.models import IceCream

def index(request):
    template_name = 'homepage/index.html'
    # Запрос:
    ice_cream_list = IceCream.objects.all()
    # Полученный из БД QuerySet передаём в словарь контекста:
    context = {
        'ice_cream_list': ice_cream_list,
    }
    # Словарь контекста передаём в шаблон, рендерим HTML-страницу:
    return render(request, template_name, context)

def ice_cream_detail(request, pk):
    template_name = 'ice_cream/detail.html'
    ice_cream = get_object_or_404(
        IceCream.objects.select_related(
            'category').values(
            'title', 'description'
        ).filter(is_published=True),
        pk=pk)
    context = {
        'ice_cream': ice_cream,
    }
    return render(request, template_name, context)


def ice_cream_list(request):
    template = 'ice_cream/list.html'
    context = {}
    return render(request, template, context)
