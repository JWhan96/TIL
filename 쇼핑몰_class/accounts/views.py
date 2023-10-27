from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm # 지금당장은 아이디/패스워드만 로그인하므로 커스텀안해도댐, 이메일로 로그인 기능넣으려면 커스텀
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
# Todo : 회원가입 기능 구현 예정
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # 회원가입
            user = form.save()
            # 로그인 후 리다이렉트
            auth_login(request, user)
            return redirect('shop:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)


# Todo : 로그인 기능 구현 예정
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('shop:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)


# Todo : 로그아웃 기능 구현 예정
def logout(request):
    auth_logout(request)
    return redirect('shop:index')


# Todo : 프로필 기능 구현 예정
def profile(request, user_pk):
    
    return render(request, 'accounts/profile.html')
    