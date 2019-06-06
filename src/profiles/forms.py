from django import forms
from .models import Profile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'employeeID',
            'phone',
        ]

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model =Profile
        fields = [
            'phone',
        ]