from django.db import models
from django.conf import settings
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    # 이미지 URL을 저장
    image = models.URLField()
    # 장바구니(product:User = M:N)
    # user.product_set -> 역참조시 이름 -> related_name을 지정해서 편하게 역참조시 사용할 이름
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='cart', blank=True)