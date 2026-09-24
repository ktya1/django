from django.contrib import messages
from django.shortcuts import redirect, render
# from models import Us
from users.forms import UserForm
from django.contrib.auth import authenticate, login, logout

from users.models import User
# Create your views here.

def login_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('users-profile')
            else:
                messages.error(request, 'неверное имя пользователя или пароль')



    else:
        form = UserForm()

    return render(request, 'users/login.html', {'form': form})



def register_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']


            user = User.objects.filter(username = username).exists()

            if user:
                messages.error(request, 'пользователь существует')
            else:

               User.objects.create_user(username=username, password=password)
               messages.success(request, 'регистрация прошла успешно')
               return redirect('users-login')

    else:
        form = UserForm()

    return render(request, 'users/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('users-login')

def profile_view(request):
    return render(request, 'users/profile.html', {'user' : request.user})