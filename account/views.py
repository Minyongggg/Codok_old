from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# from .models import 
from django.contrib import admin, auth
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request, '2_home/home.html')


def signup(request):
    if (request.method == 'POST'):
        find_user = User.objects.filter(username=request.POST['username'])
        if (find_user):
            error = '중복되는 아이디입니다.'
            return render(request, '0_registration/signup.html', {'error': error})

        new_user = User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password'],
        )
        auth.login(request, new_user)
        return redirect('home')

    return render(request, '0_registration/signup.html')

def login(request):
    if (request.method == 'POST'):
        login_user = auth.authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if (login_user is None):
            error = '아이디 또는 비밀번호가 틀렸습니다.'
            return render(request, '0_registration/login.html', {'error': error})
        auth.login(request, login_user)
        return redirect('home')

    return render(request, '0_registration/login.html')

def logout(request):
    auth.logout(request)

    return redirect('home')

