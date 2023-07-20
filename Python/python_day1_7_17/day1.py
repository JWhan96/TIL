a = 1
b = 2
c = a + b
# c가 나중에 등장했을때 알기 힘듦

num1 = 1
num2 = 2
sum_result = num1 + num2
# 어떤 변수 인지 유추가능

temp = 25
is_hot = temp > 30
# is_***의 경우 TRUE/FALSE의 값을 의미

numbers = [1, 2, 3, 4, 5]
student_grades = [24, 74, 61]
# 변수의 경우 단수 복수 구별해주면 좋음

# 시간 예시
seconds = 60
minute = 60 
hours = 24
# 이런 값들은 이미 정해져 있다 (상수)
#상수/변하지 않는 값이므로 대문자로 표현
SECONDS = 60
MINUTE = 60
HOURS = 24 
# 변수값을 알기 쉽게 표현해주면 더 좋음
SECONDS_PER_MINUTE = 60

# 변수와 연산자 사이는 띄어쓰기
result = 2 + 3 * (2 - 3)

'''
여러줄 주석
2번째줄
'''


char = input()
# 문자열로 입력
char = input('문자 한개를 입력하세요!:')
#입력시 문구
num = int(input())
# 정수로 입력하기

char1, char2 = input().split()
#공백을 기준으로 변수 두개 한번에 입력받기
num1, num2 = map(int, input().split())
#동시에 정수화까지
year, month, day = map(int, input().split('.'))
#2023.7.17형식으로 입력받고 .기준으로 나누어 각각 배열

num_list = list(map(int, input().split()))
print(num_list)
#리스트 형식으로 받는 방법


name = input()
age = int(input())
height = float(input())
# 1. 포맷방법 1
print('저의 이름은 %s, 나이는 %d, 키는 %.2f' %(name, age, height) )
#%s는 문자열 %d는 정수 %.2f는 실수(소숫점 둘째자리까지 반올림, 기본적으론 6자리)
# 입력받은 변수 출력방법

# 2. f-string
print(f'저의 이름은 {name}, 나이는 {age}, 키는 {height:.2f}')
##이 방법을 가장 많이 쓸 것이다.-> 변수가 많아질 수록 정확해진다.

# 3. .format()
print("저의 이름은 {}, 나이는 {}, 키는 {:.2f}".format(name, age, height))