from django import forms
from .models import Item, Color, Building, Category
import datetime
from .fields import GroupedModelChoiceField


RETRIEVE_STATUS = [
    (False, "Not Retrieved"),
    (True, "Retrieved"),
]

class ShowItemForms(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'category',
            'building',
            'room',
            'date',
            'color',
            'description',
            'image',
            'retrieved'
        ]

    category = GroupedModelChoiceField(
                queryset=Category.objects.exclude(parent=None), 
                choices_groupby='parent'
        )
    color = forms.ModelChoiceField(queryset=Color.objects.all())
    date = forms.DateField(
        widget=forms.DateInput(format='%m/%d/%Y',
            attrs={
                "placeholder":"MM/DD/YYYY"
            }
        ))
    building = GroupedModelChoiceField(
                queryset=Building.objects.exclude(parent=None), 
                choices_groupby='parent'
        )
    room = forms.CharField(required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder":"Room"
            }
        )
    )
    retrieved_date = forms.DateField(required=False,
        widget=forms.DateInput(format='%m/%d/%Y',
            attrs={
                "placeholder":"MM/DD/YYYY",
            }
        ))
    retrieved = forms.ChoiceField(choices = RETRIEVE_STATUS,
                             widget=forms.Select())

class RegisterItemForms(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'category',
            'building',
            'room',
            'date',
            'color',
            'description',
            'image',
            'register_user'
        ]
    category = GroupedModelChoiceField(
                queryset=Category.objects.exclude(parent=None), 
                choices_groupby='parent'
        )
    color = forms.ModelChoiceField(queryset=Color.objects.all())
    date = forms.DateField(required=False,
        widget=forms.DateInput(format='%m/%d/%Y',
            attrs={
                "placeholder":"MM/DD/YYYY"
            }
        )
    )
    image = forms.ImageField(required=True)
    building = GroupedModelChoiceField(
                queryset=Building.objects.exclude(parent=None), 
                choices_groupby='parent'
        )
    room = forms.CharField(required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder":"Room"
            }
        )
    )

class SearchItemForms(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'building',
            'room',
            'color',
            'category',
            'retrieved',
        ]
    from_date = forms.DateField(required=False,
        widget = forms.DateInput(
            attrs = {
                'placeholder':"MM/DD/YYYY"
            }
        )
    )
    to_date = forms.DateField(required=False,
        widget = forms.DateInput(
            attrs = {
                'placeholder':"MM/DD/YYYY"
            }
        )
    )
    category = GroupedModelChoiceField(
                queryset=Category.objects.exclude(parent=None), 
                choices_groupby='parent'
        )
    retrieved = forms.ChoiceField(choices = RETRIEVE_STATUS,
                            widget=forms.Select(),
                            )
    building = GroupedModelChoiceField(
                queryset=Building.objects.exclude(parent=None), 
                choices_groupby='parent'
        )
    room = forms.CharField(required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder":"Room"
            }
        )
    )
    color = forms.ModelChoiceField(queryset=Color.objects.all(), required=False)