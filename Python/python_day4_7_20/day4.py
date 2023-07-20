##제어문(Control Statement)
#코드의 실행 흐름을 제어하는데 사용 '조건'에 따라 코드 블록을 실행하거나 '반복'적으로 코드를 실행

##조건문(Conditional Statement)
#주어진 조건식을 평가, 해당 조건이 참(True)인 경우에만 실행하거나 건너뜀

#사용되는 키워드
#if/ elif/ else

#복수조건문
#조건식을 동시에 검사하는 것이 아니라 순차적으로 비교
dust = 35 

if dust > 150:
    print('매우 나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')  #여기까지 내려옴
else:
    print('좋음')  #else는 상관 X
    
#중첩 조건문
dust = 400
if dust > 150:
    print('매우 나쁨')    #여기 조건에서 True
    if dust > 300:
        print('위험해요! 나가지마세요!')  #한번더 True 두개 출력
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else :
    print('좋음')


##반복문(Loop Statement)
# 주어진 코드 블록을 여러 번 반복해서 실행하는 구문
# 특정 작업을 반복적으로 수행 / 주어진 조건이 참인 동안 반복

##"for" statement
#임의의 '시퀀스'의 항목들을 그 시퀀스에 들어있는 순서대로 반복

#for문의 기본구조
'''
for 변수 in 반복가능한 객체:
    코드블록
'''
# *반복가능한 객체(iterable)
# 반복문에서 순회할 수 있는 객체: 시퀀스 객체 뿐만 아니라 dict, set등도 포함

#문자열 순회
strs = 'stars'
for i in strs:
    print(i)
#리스트 순회
lists = ['er', 'rr', 'wr']
for i in lists:
    print(i)
#인덱스로 리스트 순회
for i in range(len(lists)):
    print(i)

#중첩된 반복문
outers = ['A', 'B']
inners = ['c', 'd']

for outer in outers:
    for inner in inners:
        print(outer, inner)
'''
A c   처음 요소에 대해서 outers, inners 출력
A d   바깥으로 나가는 것이 아니라 안쪽 for문이 끝날때까지 안쪽 반복
B c   안쪽 for끝나고 바깥쪽 2번째 시작
B d   다시 안쪽 for문 끝날때까지 반복

안쪽 반복문은 outers 리스트의 각 항목에 대해 한 번씩 실행됨
print가 호출되는 횟수 => len(outers) * len(inners)

'''

#중첩 리스트 순회
#안쪽 리스트 요소에 접근하려면 바깥 리스트를 순회하면서 중첩 반복을 사용, 각 안쪽 반복을 순회

elements = [['A', 'B'], ['c', 'd']]

for elem in elements:
    print(elem)
'''
['A', 'B']
['c', 'd'] elements의 요소까지만 출력
'''
for elem in elements:
    for item in elem:
        print(item)
'''
A
B
c
d  설명 추가(여기서 영상에서IM설명함)
'''

##while
# 주어진 조건식이 참(True)인 동안 코드를 반복해서 실행
# ==조건식이 거짓(False)가 될 때까지 반복

#while문의 구조
'''
while 조건식:
    코드 블록
'''
#while 반복문 예시
a = 0

while a < 3:
    print(a)
    a += 1

print('끝')
'''
0
1
2  #3까지 증가는 한다 다시 while문으로 돌아가고 False가 되므로 while문 탈출
끝 #탈출 후 출력
'''

#사용자 입력에 따른 반복
number = int(input('양의 정수를 입력: '))

while number <= 0 :
    if number < 0:
        print('음수 입력')
    else :
        print('0입니다')
    number = int(input('양의 정수를 입력: '))
print('Good')
'''
양의 정수를 입력: 0
0입니다
양의 정수를 입력: -1
음수 입력
양의 정수를 입력: 1  #양의 정수이므로 while탈출
Good
'''

# ***while문은 반드시 종료조건이 필요!

#for
## 반복 횟수가 명확하게 정해져 있는 경우 유용
## 예를 들어 리스트, 튜플, 문자열 등과 같은 시퀀스 형식의 데이터를 처리할 때 

#while
## 반복횟수가 불명확하거나 조건에 따라 반복을 종료해야 할 때 유용
## 예를 들어 사용자의 입력을 받아서 특정조건이 충족이 될때까지 반복하는 경우

##break
#예시
numbers = [1, 3, 5, 6, 7, 9, 10, 11]
found_even = False

for num in numbers:
    if num % 2 == 0:
        print('짝수 찾음: ', num)
        found_even = True
        break
if not found_even:
    print('짝수 없음')
'''
짝수 찾음:  6
첫번째 짝수를 만난 후 for문이 break되어서 7이후부터는 반복 x
found_even도 True로 바뀌어서 짝수없음이 프린트 되지않음
만약 짝수가없으면 짝수없음이 for문이 끝난후에 프린트
'''
## continue
# 예시(홀수만 출력)
numbers = [1, 3, 5, 6, 7, 9, 10, 11]

for num in numbers:
    if num % 2 == 0:
        continue
    print(num)
'''
1
3
5
7
9
11
'''


##리스트 생성방법
#1. []
#2. map+list
#3. List Comprehension: 간결하고 효율적인 리스트 생성 법
#구조
'''
[expression for 변수 in iterable]
list(expression for 변수 in iterable)
'''
#0~9 요소를 가지는 리스트 만들기
#1. 일반적인 방법
new_list = []
for i in range(10):
    new_list.append(i)
print(new_list) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#조건추가
new_list = []
for i in range(10):
    if i % 2 == 1:
        new_list.append(i)

print(new_list)

# 2. list comprehension
new_list_2 = [i for i in range(10)]
new_list_3 = [i if i % 2 == 1 else str(i) for i in range(10)]
print(new_list_2)

# 조건추가
new_list_2 = [i for i in range(10) if i % 2 == 1]
print(new_list_2)

##if else들어가는 경우
new_list_3 = [i if i % 2 == 1 else str(i) for i in range(10)]

new_list_4 = []
for i in range(10):
    if i % 2 == 1:
        new_list_4.append(i)
    else:
        new_list_4.append(str(i))
print(new_list_4)
##List comprehension의 경우 가독성이 떨어질 수 가 있다
#두개를 알아 보고 바꿀 수 있어야하지만
#List comprehension을 남용하지는 말자

##리스트를 생성하는 3가지 방법 빅
# 정수 1, 2, 3을 가지는 새로운 리스트 만들기
# 어떤게 제일 빠른가- 어떻게 잘쓰는지만 잘 알면 댄다.
# 우리 프로그램이 어떻게 그 목적을 명확하게 전달하는지가 더 중요
# "작은 효율성에 대해서는, 말하자면 97%정도에 대해서는 잊어버려라
# 섣부른 최적화는 모든 악의 근원이다."-도널드 knuth
numbers = ['1', '2', '3']

# 1. for loop
new_numbers = []
for number in numbers:
    new_numbers.append(int(number))
print(new_numbers)

# 2. map
new_numbers_2 = list(map(int, numbers))
print(new_numbers_2)

# 3.list comprehension
new_numbers_3 = [int(number) for number in numbers]
print(new_numbers_3)


##pass
# 1. 코드 작성중 미완성 부분
# 구현해야 할 부분이 나중에 추가될 수 있고, 코드를 컴파일하는 동안 오류가 발생하지 않음

# 2. 조건문에서 아무런 동작을 수행하지 않아야 할 때

# 3. 무한루프에서 조건이 충족되지 않을 때 pass 를 사용하여 루프를 계속 진행하는 방법
 ##continue랑의 차이???

#enumerate(iterable, start=0)
#iterable 객체의 각 요소에 대해 인덱스와 함께 반환하는 내장함수
result = ['a', 'b', 'c']

print(enumerate(result))
print(list(enumerate(result)))
#[(0, 'a'), (1, 'b'), (2, 'c')]  튜플로 출력

for index, elem in enumerate(result):
    print(index, elem)
#인덱스 값과 요소값을 같이 출력할때 enumerate자주 사용