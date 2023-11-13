from django import forms
from django.contrib.auth.forms import UserCreationForm

from authentication.models import Customer


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ["username", "password1", "password2"]
