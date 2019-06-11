from django.contrib import admin
from .models import Item, Color, Building, Category
# Register your models here.
admin.site.register(Item)
admin.site.register(Color)
admin.site.register(Building)
admin.site.register(Category)