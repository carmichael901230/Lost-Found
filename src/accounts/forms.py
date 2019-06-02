from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from profiles.models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'email',
        ]
        
    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'employeeID',
            'phone',
        ]
