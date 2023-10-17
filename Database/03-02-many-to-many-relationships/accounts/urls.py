from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('profile/<str:username>/', views.profile, name='profile'),
    # path('<username>/', views.profile, name='profile'), # 이렇게 작성하면 유저네임 이후에 들어오는 문자열로 받는다면 인식을 하지 못한다, 다 그냥 유저네임으로 인식
    path('<int:user_pk>/follow/', views.follow, name ='follow'),
]
