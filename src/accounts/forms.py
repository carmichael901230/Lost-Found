from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    employeeID = forms.IntegerField(required=True)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'username',
            'employeeID',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'email',
        ]

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.employeeID = self.cleaned_data['employeeID']
        user.last_name = self.cleaned_data['last_name']
        user.first_name = self.cleaned_data['first_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user