from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from .models import SitePage

def page_view(request, slug):
    page = get_object_or_404(SitePage, slug=slug)
    return render(request, 'page.html', {
        'page': page,
        'from_site_pages': True  # этот флаг важен
    })

def site_pages_links(request):
    return {
        'site_pages': SitePage.objects.all()
    }


def base(request):
    page, created = SitePage.objects.get_or_create(
        slug='start',
        defaults={
            'title': 'Добро пожаловать',
            'content': 'Это стартовая страница сайта. Её можно изменить в админке.'
        }
    )
    return render(request, 'page.html', {'page': page, 'from_site_pages': True})

