from django.contrib import admin
from .models import Item, Color, Building, Category

class ItemAdmin(admin.ModelAdmin):
    list_display = ('category', 'color', 'building', 'date', 'description')
    
# Register your models here.
admin.site.register(Item, ItemAdmin)
admin.site.register(Color)
admin.site.register(Building)
admin.site.register(Category)