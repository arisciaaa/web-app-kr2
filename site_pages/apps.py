from django.apps import AppConfig
from django.db.utils import OperationalError
from django.core.exceptions import ImproperlyConfigured

class SitePagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'site_pages'

    def ready(self):
        from django.db.models.signals import post_migrate
        from .models import SitePage

        def create_default_page(sender, **kwargs):
            try:
                if not SitePage.objects.filter(slug='start').exists():
                    SitePage.objects.create(
                        title='Главная страница',
                        slug='start',
                        content='<p>Это стартовая страница по умолчанию.</p>'
                    )
            except (OperationalError, ImproperlyConfigured):
                # База данных ещё не готова, пропускаем
                pass

        post_migrate.connect(create_default_page, sender=self)
