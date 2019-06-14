from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from profiles.models import Profile

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=20,
        widget=forms.PasswordInput(
            attrs={
                'class':"form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':"form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':"form-control"
            }
        )
    )
    email = forms.EmailField(required=False,
        widget=forms.TextInput(
            attrs={
                'class':"form-control",
                'size':30
            }
        )
    )
    first_name = forms.CharField(max_length=20,
        widget=forms.TextInput(
            attrs={
                'class':"form-control"
            }
        )
    )
    last_name = forms.CharField(max_length=20,
        widget=forms.TextInput(
            attrs={
                'class':"form-control"
            }
        )
    )

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

class UserEditForm(UserChangeForm):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class':"form-control",
                'size':30
            }
        )
    )
    first_name = forms.CharField(max_length=20,
        widget=forms.TextInput(
            attrs={
                'class':"form-control"
            }
        )
    )
    last_name = forms.CharField(max_length=20,
        widget=forms.TextInput(
            attrs={
                'class':"form-control"
            }
        )
    )
    
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email'
        ]
    