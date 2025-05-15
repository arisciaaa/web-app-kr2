from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import SitePage

@admin.register(SitePage)
class SitePageAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "created_at", "order")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}
