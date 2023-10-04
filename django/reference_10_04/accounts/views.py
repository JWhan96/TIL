from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# Create your views here.
def index(request):
    
    return render(request, 'accounts/index.html')


def login(request):
    if request.method == 'POST':
        # POST:실제 로그인 로직
        form = AuthenticationForm(request, request.POST)
        # form에 담긴 데이터가 유용하다면
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index')    
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }

    return render(request, 'accounts/login.html', context)
# 로그아웃
# 세션ID삭제, 클라이언트에게도 전달 X
def logout(request):
    auth_logout(request)
    return redirect('accounts:index')