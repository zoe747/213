from django.contrib import admin
from .models import Folder


# Register your models here.
class FolderAdmin(admin.ModelAdmin):
    list_display = ["folder_id", "folder_name", "father_folder", "owner", "group"]


admin.site.register(Folder, FolderAdmin)
