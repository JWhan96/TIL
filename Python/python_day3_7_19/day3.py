#함수
##특정 작업을 수행하기 위한 재사용 가능한 코드 묶음
##사용하는 이유
# 코드의 중복 방지
# 재사용성이 높아지고 가독성 및 유지보수성 향상
#def, return을 통해 함수 선언 가능
def get_sum(num1, num2):
    return num1 + num2
num1 = 3
num2 = 5
sum1 = get_sum(num1, num2)
print(sum1)

##내장함수: 별도의 import없이 바로 사용가능 
#ex)print(), abs()
#Python.document(3.9v) https://docs.python.org/ko/3/

#함수구조 
##사진 넣기####

def make_sum(pram1, pram2): #parameter INPUT X

    '''
    이것은 두 수를 받아
    두 수의 합을 반환하는 함수입니다.
    >>>make_sum(1, 2)
    3
    이 구조는 Docstring으로 함수에 대한 
    설명을 할 때 주로 작성
    '''
    return pram1 +pram2
# print 는 반환이 안된다.
# return키워드 이후에 반환한 값을 명시,
# 함수의 실행을 중료하고 결과를 호출 부분으로 반환
# return이 없어 반환이 안된다면 결과물은 None이 자동으로 반환된다.


#매개변수(parameter): 함수를 정의할 때 함수가 받을 값을 나타내는 변수
#인자(argument): 함수가 호출될 때 실제로 전달되는 값

def add_numbers(x, y):
    result = x + y
    return result        #x와 y는 매개변수

a = 2
b = 3
sum_result = add_numbers(a, b) #a와 b는 인자
print(sum_result)

##위치인자(Positional Arguments)
#함수 호출 시 인자의 위치에 따라 전달되는 인자(함수 호출 시 반드시 값을 전달해야함)
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요')
greet('Alice', 25)

##기본 인자 값(Default Argument Values)
#함수 정의에서 매개 변수에 기본 값을 할당하는 것
#함수 호출시 인자를 전달하지 않으면, 기본값이 매개변수에 할당됨
def greet(name, age=30):
    print(f'안녕하세요, {name}님! {age}살이시군요')
greet('Bob')
greet('Bob', 40)
greet(age=20, name='Alice') ##Keywork 인자
# greet(age=30, 'bob')
# greet('bob', age=30) 이건 가능 
#SyntaxError가 남, 주의! 키워드 인자는 위치 인자 뒤에 와야한다
#positional argument follows keyword argument
print('hello', end = ' ')####end = ' '이것도 기본인자로 쓰이던 것
print('world')
###########




##임의의 인자 목록(Arbitrary Argument Lists)
#정해지지 않은 개수의 인자를 처리하는 인자
#함수 정의시 매개변수 앞에 *를 붙여 사용, 여러개의 인자가 Tuple로 처리
# * : 별x, asterisk
def cal_sum(*args):
    print(args)
    total = sum(args)
    print(f'합계: {total}')
'''
(1, 2, 3)
합계: 6
(1, 2, 3, 4, 5)
합계: 15
'''
cal_sum(1 ,2, 3)
cal_sum(1, 2, 3, 4, 5)

##임의의 키워드 인자 목록
#정해지지 않은 개수의 키워드 인자를 처리하는 인자
#함수 정의시 매개변수 앞에 '**'를 붙여 사용,
#여러개의 인자를 dict로 묶어 처리
def print_info(**kwargs):
    print(kwargs)
'''
{'name': 'eve', 'age': 30}
'''
print_info(name = 'eve', age = 30)

##함수 인자 권장 작성순서
#위치 -> 기본 -> 가변 -> 키워드 ->가변키워드
# 절대적인 규칙은 아니며, 상황에 따라 유연하게 조정가능
#단!! 키워드인자랑 위치인자는 같이 사용할 수 없다!

##Python의 범위(scope)
#함수는 코드 내부에 local scope, 그 외 공간은 global scope
num = 3 #global scope
def my_num():
    num = 1 #로컬변수
    print(num)
    '''
    local scope
    함수내에서는 바깥 scope의 변수에 접근은 가능, 수정 x
    '''

def my_num2():

    print(num)
    '''
    local scope
    local scope에서 변수를 설정안해주면
    위의 영역에서 변수를 찾으러 감
    '''

my_num()
my_num2()
print(num) #global scope

#변수 수명주기(lifecycle)
# 1. built-in scope
#    파이썬이 실행된 이후부터 영원히 유지/ print()
# 2. global scope
#    모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
# 3. local scope
#    함수가 호출될 때 생성, 함수가 종료될때까지 유지

##이름 검색 규칙(Name Resolution)
#LEGB rule


#local에서 global(바깥 쪽)의 변수를 바꿀 수는 없지만
#global 함수를 사용하면 가능
#global 키워드 주의사항 선언전에 접근/매개변수에 사용
num = 0 #전역 변수

def increment():
    global num
    num += 1
print(num)
increment()
print(num)


##재귀 함수 
#특징
# 특정 알고리즘 식을 표현할 때 변수의 사용이 줄어들고, 코드의 가독성이 향상
# 1개 이상의 base case(종료되는 상황)가 존재, 수렴하도록 장성
#대표적 예시 - 팩토리얼
def factorial(n):
    # 종료 조건: n이 0이면 1을 반환! 무한루프에 빠지지 않도록
    if n==0:
        return 1
    
    return n*factorial(n-1)

result = factorial(5)
print(result)

##map


##lambda



##map + lambda
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2 , numbers))
print(result)
#일회성으로 사용하는 경우 람다 함수를 사용함
numbers = [1, 2, 3, 4, 5]

def double_number(x):
    return x * 2

result = list(map(double_number, numbers))
print(result)


##패킹 : 여러 값을 하나의 시퀀스로 묶는 과정(튜플 형태로 묶임)
# 예시 1)
packing_values = 1, 2, 3, 4, 5
print(packing_values)  # (1, 2, 3, 4, 5)

numbers = [1, 2, 3, 4, 5] # *(에스터리스크): 패킹연산자로 활용 나머지를 리스트로 패킹
a, *b, c = numbers
print(a) # 1
print(b) # [2, 3, 4]
print(c) # 5

print('hi', 'hello', 'goodbye', sep = '-') #hi-hello-goodbye
print('hi', end = '')
print('hello')   #hihello

# *(에스터리스크)를 언패킹 연산자로 활용
names = ['kai', 'jane', 'bob']
print(*names)   #kai jane bob

# **: 딕셔너리 언패킹 연산자
def my_function(x, y, z):
    print(x, y, z)
dict_values = {'x' : 1, 'y' : 2, 'z' : 3}
my_function(**dict_values)   #1 2 3


##모듈
#모듈과 라이브러리는 같은 말이다? (x)
#라이브러리는 모듈과 패키지의 집합이다
#예시1
import math  #ctrl + math클릭  math에 대해서 설명나옴(파이썬 제공모듈)
print(math.pi)
print(math.sqrt(4))
#예시2
from math import pi, sqrt
print(pi)
print(sqrt(4))
#예시3
import random
print(random.randint(1, 10))
#예시4
from random import *  #ㅊㅇimport *: 랜덤모듈로부터 모든 걸 가지고 오겠다.
print(randint(1, 10))

#my_math 사용자 정의 모듈 생성
# import my_math
# print(my_math.add(1, 5)) ##add함수를 my_math에 저장/위치 옮겨서 오류

from my_package.math import my_math
from my_package.statistics import tools
##from 상위폴더.하위폴더 import 패키지
print(my_math.add(1, 2))
print(tools.mod(4, 3))