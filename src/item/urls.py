from django.urls import path
from .views import (
    show_item_view,
    register_item_view,
    search_item_view
)

app_name = "items"
urlpatterns = [
    path('register/', register_item_view, name="register_item"),
    path('item/<int:item_id>/', show_item_view, name="show_item"),
    path('search/', search_item_view, name="search_item"),
]

