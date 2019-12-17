from django.contrib import admin
from .models import Office


class OfficeAdmin(admin.ModelAdmin):
    list_display = ['office']
    list_display_links = ['office']
    search_fields = ['office']
    list_per_page = 25


admin.site.register(Office, OfficeAdmin)

