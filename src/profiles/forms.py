from django import forms
from .models import Profile

class UserProfileForm(forms.ModelForm):
    phone = forms.CharField(max_length=20, required=False,
        widget=forms.TextInput(
            attrs={
                'class':"form-control"
            }
        )
    )
    employeeID = forms.CharField(max_length=10,
        widget=forms.TextInput(
            attrs={
                'class':"form-control",
                'size':10
            }
        )
    )
    class Meta:
        model = Profile
        fields = [
            'employeeID',
            'phone',
        ]

class ProfileEditForm(forms.ModelForm):
    phone = forms.CharField(max_length=20, required=False,
        widget=forms.TextInput(
            attrs={
                'class':"form-control"
            }
        )
    )
    class Meta:
        model =Profile
        fields = [
            'phone',
        ]