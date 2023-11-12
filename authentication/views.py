from django.contrib.auth.models import User
from .models import Customer
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from authentication.forms import UserRegisterForm
from django.urls import reverse_lazy

class RegisterView(CreateView):
    template_name = 'authentication/register.html'
    success_url = reverse_lazy('login')
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"

class LoginView(LoginView):
    template_name = 'authentication/login.html'
