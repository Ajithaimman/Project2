from django import forms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User 
from django.forms.widgets import PasswordInput,TextInput


class CreateUserForm(UserCreationForm):

    username=forms.CharField(widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "placeholder":"Enter the username"
    }),label=""),

    username=forms.CharField(widget=forms.TextInput(attrs={
        "class":"input",
        "type":"email",
        "placeholder":"Enter the email"
    }),label=""),

    username=forms.CharField(widget=forms.TextInput(attrs={
        "class":"input",
        "type":"password",
        "placeholder":"Enter the password"
    }),label=""),

    username=forms.CharField(widget=forms.TextInput(attrs={
        "class":"input",
        "type":"password",
        "placeholder":"Enter the password again"
    }),label=""),

    class Meta:
        model=User
        fields=['username','email','password1','password2']

class LoginForm(AuthenticationForm):
    # username=forms.CharField(widget=TextInput())
    # password=forms.CharField(widget=PasswordInput())

    username=forms.CharField(widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "placeholder":"Enter the username"
    }),label=""),

    password=forms.CharField(widget=forms.TextInput(attrs={
        "class":"input",
        "type":"password",
        "placeholder":"Enter the password"
    }),label=""),



