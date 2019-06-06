from django import forms
from .models import Item

class ShowItemForms(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'category',
            'building',
            'room',
            'date',
            'time' ,
            'color',
            'description',
            'image',
            'retrieved'
        ]
    CHOICES = [
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
    category = forms.ChoiceField(choices=CHOICES)
    