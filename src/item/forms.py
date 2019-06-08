from django import forms
from .models import Item
import datetime

CATE_CHOICES = [
    ("Electronics",(
        (1,"Flash Drives"),
        (2,"Phones"),
        (3,"Calculators"),
        (4,"Laptops/PC"),
        (5,"Chargers/Cabels"),
        (6,"Power Banks"),
        (7,"Headphones/Earbuds"),
        (9,"Other Electronics")
    )),
    ("Books",(
        (11,"Textbooks"),
        (12,"Notebooks"),
    )),
    ("Cards",(
        (21,"ID Cards"),
        (22,"Credit/Debit Cards"),
        (29,"Other Cards")
    )),
    ("Office Products",(
        (31,"Pens/Pencils"),
        (32,"Erasers"),
        (33,"Rulers"),
        (34,"Sharpeners"),
        (35,"Binders"),
        (36,"Bottles"),
        (39,"Other Office Products")
    )),
    ("Clothing & Accessories",(
        (41,"Clothes"),
        (42,"Pants"),
        (43,"Shoes"),
        (44,"Hats"),
        (45,"Watches"),
        (46,"Glasses"),
        (49,"Other Accessories")
    )),
]

COLOR_CHOICES = [
    ('white',"White"),
    ('grey',"Grey"),
    ('black',"Black"),
    ('blue',"Blue"),
    ('green',"Green"),
    ('yellow',"Yellow"),
    ('orange',"Orange"),
    ('red',"Red"),
    ('pink',"Pink"),
    ('purple',"Purple"),
    ('brown',"Brown")
]

RETRIEVE_STATUS = [
    (True, "Retrieved"),
    (False, "Not Retrieved")
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

    category = forms.ChoiceField(choices=CATE_CHOICES)
    color = forms.ChoiceField(choices=COLOR_CHOICES)
    date = forms.DateField(required=False,
        widget=forms.DateInput(format='%m/%d/%Y',
            attrs={
                "placeholder":"MM/DD/YYYY"
            }
        ))
    building = forms.CharField(required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder":"Building"
            }
        )
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
                              initial='', widget=forms.Select())

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
    category = forms.ChoiceField(choices=CATE_CHOICES)
    color = forms.ChoiceField(choices=COLOR_CHOICES)
    date = forms.DateField(required=False,
        widget=forms.DateInput(format='%m/%d/%Y',
            attrs={
                "placeholder":"MM/DD/YYYY"
            }
        ))
    building = forms.CharField(required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder":"Building"
            }
        )
    )
    room = forms.CharField(required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder":"Room"
            }
        )
    )