from django.contrib import admin
from .models import ExtraInfo
import csv
from django.http import HttpResponse
from io import StringIO


def download_csv(modeladmin, request, queryset):
    import csv
    from django.http import HttpResponse
    from io import  StringIO
    f = StringIO()
    writer = csv.writer(f)
    writer.writerow(["user", "email", "samtykke", "employment_status"])
    for s in queryset:
        writer.writerow([s.user, s.email, s.samtykke, s.employment_status])
    f.seek(0)
    response = HttpResponse(f, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=extra-info.csv'
    return response    

class ExtraInfoAdmin(admin.ModelAdmin):  
    actions = ['download_csv']  
    list_display = ('user', 'email', 'samtykke', 'employment_status',)
    list_display_links = ('user', 'email','employment_status',)
    list_filter = ('user',)
    search_fields = ('user', 'email', 'samtykke', 'employment_status',)
    list_per_page = 25  
    def download_csv(self,modeladmin, request, queryset):
        None  
    download_csv.short_description = "Last ned som CSV."

    
admin.site.register(ExtraInfo, ExtraInfoAdmin)
