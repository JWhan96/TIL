from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm
# Create your views here.


def login(request):
    if request.method == 'POST':
        
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data = request.POST)
        if form.is_valid(): # 통과했을때
            # 로그인/ 함수이름과 똑같으므로 login이 아닌 auth_login으로 
            auth_login(request, form.get_user())
            
            # next_url 처리
            next_url = request.POST.get('next')
            
            
            if next_url:
                return redirect(next_url)
            
            
            return redirect('movies:index')

    
    
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('movies:index')

def signup(request):
    #장고의 기본 user모델 기반으로 동작
    # -> 버그 발생
    # form = UserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # form.save()
            # 1. DB에 유저 저장
            # 2. 내가 현재 저장하고자 하는 객체를 반환
            user = form.save()
            auth_login(request, user)
            # 회원가입하자마자 로그인
            return redirect('movies:index')
    
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)

def delete(request):
    request.user.delete()
    return redirect('movies:index')

@login_required
def update(request):
    
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance= request.user)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = CustomUserChangeForm(instance= request.user)
    context = {
        'form' : form
    }
    return render(request, 'accounts/update.html', context)


def change_password(request, user_pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('movies:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/change_password.html', context)