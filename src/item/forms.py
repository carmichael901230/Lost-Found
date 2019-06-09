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
        (12,"Notebooks")
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
    ("Others", (
        (99, "Others"),
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

BUILDING_CHOICES = [
    ("Buildings", (
        (1, "Alumni Hall"),
        (2, "Campbell Dome"),
        (3, "Colden Auditorium"),
        (4, "Colwin Hall"),
        (5, "Continuing Ed"),
        (6, "Delany Hall"),
        (7, "Dining Hall"),
        (8, "FitzGerald Gym"),
        (9, "Frese Hall"),
        (10, "G Building"),
        (11, "Gertz Center"),
        (12, "Goldstein Theatre"),
        (13, "Honors Hall"),
        (14, "I Building"),
        (15, "Jefferson Hall"),
        (16, "Kiely Hall"),
        (17, "King Hall"),
        (18, "Kissena Hall"),
        (19, "Klapper Hall"),
        (20, "Music Building"),
        (21, "Powdermaker Hall"),
        (22, "Queens Hall"),
        (23, "Rathaus Hall"),
        (24, "Razran Hall"),
        (25, "Remsen Hall"),
        (26, "Rosenthal Library"),
        (27, "Science Building"),
        (28, "Student Union"),
        (29, "Tech Incubator"),
        (30, "The Summit"),
        (39, "Other Buildings"),
    )),
    ("Fields/Courts", (
        (41, "Track & Soccer Fields"),
        (42, "Lacrosse Field"),
        (43, "Baseball Field"),
        (44, "Softball Field"),
        (45, "Tennis Courts"),
        (49, "Other Fields/Courts"),
    )),
    ("Others", (
        (99, "Others"),
    )),
]

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

    category = forms.ChoiceField(choices=CATE_CHOICES)
    color = forms.ChoiceField(choices=COLOR_CHOICES)
    date = forms.DateField(
        widget=forms.DateInput(format='%m/%d/%Y',
            attrs={
                "placeholder":"MM/DD/YYYY"
            }
        ))
    building = forms.ChoiceField(choices = BUILDING_CHOICES,
                             widget=forms.Select())
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
    category = forms.ChoiceField(choices=CATE_CHOICES)
    color = forms.ChoiceField(choices=COLOR_CHOICES)
    date = forms.DateField(required=False,
        widget=forms.DateInput(format='%m/%d/%Y',
            attrs={
                "placeholder":"MM/DD/YYYY"
            }
        )
    )
    image = forms.ImageField(required=True)
    building = forms.ChoiceField(choices = BUILDING_CHOICES,
                            widget=forms.Select())
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
    category = forms.ChoiceField(choices=CATE_CHOICES)
    retrieved = forms.ChoiceField(choices = RETRIEVE_STATUS,
                            widget=forms.Select(),
                            )
    building = forms.ChoiceField(choices=BUILDING_CHOICES, required=False,
                            widget=forms.Select()
                            )
    room = forms.CharField(required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder":"Room"
            }
        )
    )
    color = forms.ChoiceField(choices=COLOR_CHOICES, required=False)