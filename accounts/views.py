from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from .forms import LoginForm , UpdateUserForm , UpdateProfileForm
from django.contrib.auth.decorators import login_required
from .models import Profile , Cource




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

@login_required
def home(request):
    return render(request , 'home.html' , {
    })


def update_profile(request):
    user_form = UpdateUserForm(instance=request.user)
    profile_form = UpdateProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST , instance=request.user)
        profile_form = UpdateProfileForm(request.POST , request.FILES , instance=request.user.profile)
        if user_form.is_valid and profile_form.is_valid():
            user_form.save() 
            profile_form.save()
            return redirect('accounts:home')

    return render(request , 'update_profile.html', {
        'user_form' : user_form ,
        'profile_form' : profile_form
    })


def Logout(request):
    logout(request)
    return render(request, 'logout.html')


def cources(requert , id):
    cor = Cource.objects.filter(user=id)
    return render(requert, 'cources.html' , {
       'cor' : cor ,
    })


