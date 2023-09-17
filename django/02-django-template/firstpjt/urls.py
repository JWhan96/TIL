"""
URL configuration for firstpjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', views.index, name='index'),
    path('dinner/', views.dinner, name="dinner"),
    path('search/', views.search, name="search"),
    path('throw/', views.throw, name= 'throw'),
    path('catch/', views.catch, name= 'catch'),
    # <타입:변수명>
    path('hello/<str:name>/', views.greeting, name='greeting'),
    path('articles/<int:num>/', views.detail),
    path('articles/<str:name>/', views.detaill),
    path('articles/', include('articles.urls')),
]
