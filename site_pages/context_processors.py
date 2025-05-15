from .models import SitePage

def site_pages_links(request):
    return {
        'site_pages': SitePage.objects.all()
    }