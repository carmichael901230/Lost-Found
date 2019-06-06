from django.urls import path
from .views import show_item_view

app_name = "items"
urlpatterns = [
    path('item/<int:item_id>/', show_item_view, name="show_item")
]

