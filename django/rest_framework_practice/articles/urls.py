from django.urls import path
from . import views


urlpatterns = [
    path('articles/', views.index),
    path('articles/<int:articles_pk>/', views.detail),
]
