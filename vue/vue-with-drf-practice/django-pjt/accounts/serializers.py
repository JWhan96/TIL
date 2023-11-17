from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter, DefaultAccountAdapter


class CustomRegisterSerializer(RegisterSerializer):
    # 나머지 필드들은 RegisterSerializer 에 존재
    # 회원가입시 추가로 필요한 필드들을 모두 정의
    nickname = serializers.CharField(required=False, allow_blank=True, max_length=250)
    
    
    def get_cleaned_data(self):
        return {
        'username': self.validated_data.get('username', ''),
        'password1': self.validated_data.get('password1', ''),
        'email': self.validated_data.get('email', ''),
        'nickname': self.validated_data.get('nickname', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user = adapter.save_user(request, user, self, commit=False)
        # if "password1" in self.cleaned_data:
        #     try:
        #         adapter.clean_password(self.cleaned_data['password1'], user=user)
        #     except DjangoValidationError as exc:
        #         raise serializers.ValidationError(
        #             detail=serializers.as_serializer_error(exc)
        #         )
        user.save()
        self.custom_signup(request, user)
        # setup_user_email(request, user, [])
        return user