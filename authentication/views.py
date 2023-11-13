from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserRegisterForm
from django.urls import reverse_lazy

class RegisterView(CreateView):
    template_name = 'authentication/register.html'
    success_url = reverse_lazy('login')
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"

class LoginShopView(LoginView):
    template_name = 'authentication/login.html'

class LogoutShopView(LogoutView):
    pass
