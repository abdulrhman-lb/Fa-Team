from django.shortcuts import render
from .models import Login
from django.contrib.auth import authenticate, login
from .forms import LoginForm



def login(request):
    if request.method == 'POST':
        loginn = LoginForm()
        username = request.POST['username']
        password = request.POST['password']