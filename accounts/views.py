from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def log_in(request):
    if request.user.is_authenticated:
        return redirect('/')

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home:home')
    else:
        redirect('/login')
    return render(request, 'accounts/login.html')


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('home:home')

    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create(username=username, first_name=first_name, last_name=last_name, email=email, password=password)


        if user is not None:
            login(request, user)
            return redirect('home:home')
        else:
            redirect('/signup')
    return render(request, 'accounts/signup.html', {})


def log_out(request):
    logout(request)
    return redirect('/')


