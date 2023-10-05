from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm
# Create your views here.


def login(request):
    if request.method == 'POST':
        print(f'next = {request.POST}')
        print(f'next = {request.GET}')
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data = request.POST)
        if form.is_valid(): # 통과했을때
            # 로그인/ 함수이름과 똑같으므로 login이 아닌 auth_login으로 
            auth_login(request, form.get_user())
            
            # next_url 처리
            next_url1 = request.POST.get('next')
            next_url2 = request.GET.get('next')
            
            if next_url1:
                return redirect(next_url1)
            if next_url2:
                return redirect(next_url2)
            
            return redirect('articles:index')

    
    
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')

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
            return redirect('articles:index')
    
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)

