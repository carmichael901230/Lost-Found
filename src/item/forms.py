from django import forms
from .models import Item

class ItemForms(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
                'title',
                'date',
                'time' ,
                'location',
                'color',
                'description',
                'category',
                'retrieved',
                'image'
        ]