from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile, Lecture, PLR
from django.contrib import admin, auth
from django.contrib.auth.decorators import login_required
import datetime
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from blackboard import crawling
# Create your views here.

#registration
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


# main page
@login_required(login_url='login')
def home(request):
    plrs = PLR.objects.filter(profile=request.user.profile)

    return render(request, '2_home/home.html', {'plrs': plrs})

def bblogin(request):
    if request.method == 'POST':
        bbid = request.POST['bbid']
        bbpassword = request.POST['bbpassword']
        find_id = Profile.objects.filter(portal_id=bbid)
        print(find_id is True)
        
        if(find_id):    #이미 있는 아이디
            if (request.user.profile.portal_id != bbid): #자기 아이디 아님
                error = '이미 등록된 아이디입니다.'
                return render(request, '2_home/error.html', {'error': error})
            else: # 자기 아이디임
                plrs = PLR.objects.filter(profile=request.user.profile)
                plrs.delete()
        else:       #아이디 중복 없음
            plrs = PLR.objects.filter(profile=request.user.profile)
            plrs.delete()
            Profile.objects.filter(user=request.user).update(portal_id = bbid)  #그 사람 프로필에 등록
            
        
        results = crawling(bbid, bbpassword)
        # print(results)

        if (results is False):
            error = "블랙보드 로그인 실패"
            return render(request, '2_home/error.html', {'error': error})

        if len(results) == 0:
            error = "이번 학기 강의가 없습니다"
            return render(request, '2_home/error.html', {'error': error})

        for result in results:
            PLR.objects.create(
                profile = request.user.profile,
                lecture = Lecture.objects.get(subnum=result)
            )

        return redirect('home')

        
            
        
