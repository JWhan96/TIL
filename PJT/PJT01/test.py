# import requests #requests 라이브러리 불러오기
# url = 'https://fakestoreapi.com/carts'
# #요청을 보내는 서버의 주소
# response = requests.get(url)#.json()
# # 해당서버에 데이터를 달라고 요청을 보내는 함수
# #.json(): 내부데이터를 JSON형태로 변환해주는 함수
# print(response)


import json  #내장 모듈
# json 데이터
json_data = '''
{
    'name' : '김싸피' ,
    'age' : 28 ,
    'hobbies' : [
        '공부하기',
        '복습하기'
    ]
}
'''
data = json.loads(json_data) ##json 형식의 문자열을 파싱하여 python Dintionary로 변환
print(data)
name = data['name']