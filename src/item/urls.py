from django.urls import path
from .views import show_item_view, RegisterItemView

app_name = "items"
urlpatterns = [
    path('register/', RegisterItemView, name="register_item"),
    path('item/<int:item_id>/', show_item_view, name="show_item")
]

