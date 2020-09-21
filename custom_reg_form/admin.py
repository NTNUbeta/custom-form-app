from django.contrib import admin
from .models import ExtraInfo

class ExtraInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'samtykke', 'employment_status',)
    list_display_links = ('user', 'email','employment_status',)
    list_filter = ('user',)
    search_fields = ('user', 'email', 'samtykke', 'employment_status',)
    list_per_page = 25


admin.site.register(ExtraInfo, ExtraInfoAdmin)
