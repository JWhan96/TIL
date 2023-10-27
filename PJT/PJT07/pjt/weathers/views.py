from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import requests
# Create your views here.

@api_view(['GET'])
def index(request):
    api_key = settings.API_KEY
    city = 'Seoul,KR'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url).json()

    return Response(response)