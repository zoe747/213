from django.contrib import admin
from .models import Group


# Register your models here.
class GroupAdmin(admin.ModelAdmin):
    list_display = ["group_id", "group_name", "creator"]


admin.site.register(Group, GroupAdmin)
