from django.contrib import admin
from .models import ExtraInfo
import csv
from django.http import HttpResponse
from io import StringIO

def download_csv(modeladmin, request, queryset):
    import csv
    f = open('some.csv', 'wb')
    writer = csv.writer(f)
    writer.writerow(["user", "email", "samtykke", "employment_status"])
    for s in queryset:
        writer.writerow([s.user, s.email, s.samtykke, s.employment_status])

class ExtraInfoAdmin(admin.ModelAdmin):    
    list_display = ('user', 'email', 'samtykke', 'employment_status',)
    list_display_links = ('user', 'email','employment_status',)
    list_filter = ('user',)
    search_fields = ('user', 'email', 'samtykke', 'employment_status',)
    list_per_page = 25
    actions = ['download_csv']
    download_csv.short_description = "Last ned som CSV."


    
admin.site.register(ExtraInfo, ExtraInfoAdmin)
