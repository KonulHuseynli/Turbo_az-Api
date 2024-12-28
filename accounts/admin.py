from django.contrib import admin

from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number','first_name','last_name') 
    list_per_page = 10
    search_fields = ('phone_number',)