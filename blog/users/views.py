from django.contrib import messages

from django.shortcuts import redirect, render

from users.forms import UserForm
from django.contrib.auth import authenticate, login
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



def register_view():
    ...

def logout_view():
    ...

def profile_view():
    ...