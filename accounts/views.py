from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import LoginForm



def loginform(request):
    if request.method == 'POST':
        login_form = LoginForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request , username=username , password=password)
        if user is not None:
            login(request , user)
            return redirect('accounts:home')
    else:
        login_form = LoginForm()


    return render(request , 'login.html' , {
        'login_form' : login_form ,
    })


def home(request):
    return render(request , 'home.html' , {
      
      
    })

