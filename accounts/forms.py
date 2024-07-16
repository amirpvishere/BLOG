from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"class": "form-control"}))

    def clean_password(self):
        user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        if user is not None:
            return self.cleaned_data['password']
        else:
            raise forms.ValidationError("Username or password is incorrect")


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name"}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name"}))
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "E-mail"}))

