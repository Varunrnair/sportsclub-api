from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class UserAdminConfig(UserAdmin):
    search_fields = ('email','first_name')
    
    list_display = ('email','username','first_name','is_active','is_staff')

admin.site.register(User)
admin.site.register(Player)
admin.site.register(Manager)
admin.site.register(Referee)
