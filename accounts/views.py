from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model


def log_in(request):
    if request.user.is_authenticated:
        return redirect('/')

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        redirect('/login')
    return render(request, 'accounts/login.html')


User = get_user_model()



