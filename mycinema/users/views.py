from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserForm
from .models import User


# Create your views here.


class CreateUserView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('films:list')



class LoginUserView(LoginView):
    next_page = 'films:list'
    template_name = 'users/login.html'


class LogoutUserView(LogoutView):
    next_page = reverse_lazy('films:list')





