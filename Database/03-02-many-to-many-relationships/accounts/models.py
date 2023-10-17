from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # symmetrical=True -> 참조하면 역참조도 자동으로 대칭으로 만들어줌-> follow기능은 그러면 안되므로 False
    # ManyToManyField는 중개테이블을 만드는 것 원래있는 것을 수정하는 것이 아님 -> migrate를 하더라도 default값 지정 x
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
