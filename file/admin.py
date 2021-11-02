from django.contrib import admin
from .models import File


# Register your models here.
class FileAdmin(admin.ModelAdmin):
    list_display = ["file_id", "file_name", "father_folder", "update_time", "file_type", "file_size", "owner", "group"]


admin.site.register(File, FileAdmin)
