from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

# Django 공식 문서에 권장하지 않는다고 명시되어 있음
# from .models import User



# django가 제공하는 CreationForm 을 상속 받아서
# 우리가 정의한 User 모델을 사용하도록 새로 생성

class CustomUserCreationForm(UserCreationForm):
    #닉네임을 사용할수 있도록 추가할 필드 정의
    nickname = forms.CharField(max_length=30, required=False, help_text='필요시 닉네임 입력')
    class Meta(UserCreationForm.Meta):
        # get_user_model(): 현재 프로젝트에 세팅된 User모델을 가져오는 역할
        model = get_user_model()
        # 앞으로 사용할 field는
        # 기존것 + 위에서 정의한 nickname 필드이다.
        fields = UserCreationForm.Meta.fields + ('nickname', )

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        # get_user_model() : 현재 프로젝트에 세팅된 User모델을 가져오는 역할
        model = get_user_model()
        fields = ('first_name','last_name','email',)