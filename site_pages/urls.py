from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'site_pages'
urlpatterns = [
    path('', views.base, name='base'),  # /page/
    path('<slug:slug>/', views.page_view, name='site_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
