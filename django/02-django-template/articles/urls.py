from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('articles/', views.index, name='index'),
    path('dinner/', views.dinner, name="dinner"),
    path('search/', views.search, name="search"),
    path('throw/', views.throw, name= 'throw'),
    path('catch/', views.catch, name= 'catch'),
    # <타입:변수명>
    path('hello/<str:name>/', views.greeting, name='greeting'),
]