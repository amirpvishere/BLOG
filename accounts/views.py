from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm, EditProfileForm


def log_in(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data['username'])
            login(request, user)
            redirect('accounts:login')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', context={'form': form})


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('home:home')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create(username=form.cleaned_data['username'],
                                       email=form.cleaned_data['email'],
                                       password=form.cleaned_data['password'],
                                       first_name=form.cleaned_data['first_name'],
                                       last_name=form.cleaned_data['last_name'])
            login(request, user)
            return redirect('home:home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/signup.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('home:home')


def edit_profile(request):
    form = EditProfileForm(instance=request.user)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    return render(request, 'accounts/edit_profile.html', {"form": form})



def a(request):
    a = User.objects.all()

