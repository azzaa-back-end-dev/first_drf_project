from django.contrib import admin

# Register your models here.

from common.models import *


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'file_type']
    search_fields = ['file_type']
    list_filter = ['file_type']



