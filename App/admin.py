from django.contrib import admin
from App.models import SRList, SRType

# Register your models here.

@admin.register(SRList)
class SRListAdmin(admin.ModelAdmin):
    list_display = [
        'region', 'dt', 'sr_type', 'title', 'description', 'file_upload', 'create_date', 'update_date'
    ]

@admin.register(SRType)
class SRTypeAdmin(admin.ModelAdmin):
    list_display = [
        'type'
    ]