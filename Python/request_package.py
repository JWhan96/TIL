#bash :pip install request입력/pip(파이썬 패키지 관리도구)
import requests

url = 'https://random-data-api.com/api/v2/users'

response = requests.get(url).json()
# print(response)

##https://jsonviewer.stack.hu/ 시각화 사이트

#실습) united States를 출력해 보세요

print(response['address']['country'])