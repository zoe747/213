from django.contrib import admin
from .models import User, LoginToken


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "password", "email"]


class LoginTokenAdmin(admin.ModelAdmin):
    list_display = ["user", "token"]


admin.site.register(User, UserAdmin)
admin.site.register(LoginToken, LoginTokenAdmin)
