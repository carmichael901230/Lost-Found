from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'employeeID',)

   
# Register your models here.
admin.site.register(Profile, ProfileAdmin)


