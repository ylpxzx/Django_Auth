from django.contrib import admin
from .models import *


class LoginUserAdmin(admin.ModelAdmin):
    list_display = ('phone_numbers',)


admin.site.register(LoginUser,LoginUserAdmin)
