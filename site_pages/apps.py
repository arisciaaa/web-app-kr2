from django.apps import AppConfig


class SitePagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'site_pages'

    def ready(self):
        from .models import SitePage
        if not SitePage.objects.filter(slug='start').exists():
            SitePage.objects.create(
                title='Главная страница',
                slug='start',
                content='<p>Это стартовая страница по умолчанию.</p>')

