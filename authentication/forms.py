from django import forms
from authentication.models import Customer
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = Customer
        fields = ["username", "password1", "password2"]
