#주피터 노트북...?
# 조건식에는 비교연산, 논리연산, 멤버연산 등..
# if의 부정이 elif, elif의 부정이 else

dust = int(input())

if dust > 150:
    print('매우 나쁨')
elif dust > 80:
    print('나쁨')  #elif의 범위는 80 < dust <=150
elif dust > 30:
    print('보통')  #elif의 범위는 30 < dust <=80
else:
    print('좋음')  

#실습1. 정수를 입력받아 짝수면 'even' 출력, 홀수면 'odd'출력
num1 = int(input())
if (num1 % 2) == 0:
    print('even')
else:
    print('odd')

#실습2. 윤년 판별하기, 윤년이면 'leap year', 그렇지 않으면 'common year'츨력
# 조건1. 연도가 4로 나누어 떨어지지만 100으로는 나누어 떨어지면 안된다.
# 조건2. 연도가 400으로 나누어 떨어진다.??????????????

year1 = int(input())
if (year1 % 100) != 0:
    pass

##for
#for 변수 in 반복 가능한 객체(iterable)
#반복 가능한 객체: 리스트, 튜플, 문자열, range

# 실습 1.(중첩 for문) 구구단출력
'''
<2단>
2 * 1 = 2
2 * 2 = 4
. . .
<9단>
'''
for i in range(2, 10):
    print(f'<{i}단>')
    print()  
    for j in range(1, 10):
        print(f'{i} * {j} = {i * j}')
    print()   


# 실습 2. 정수 n을 입력받아 n단의 왼쪽 직각 이등변 삼각형을 그리는 프로그램 작성

n = int(input())
print(f'n : {n}')
for i in range(1, n+1):
    print('*' * i)

#중첩for문을 사용한 같은 결과
n = int(input())
print(f'n : {n}')
for i in range(1, n+1):
    for j in range(i):
        print('*', end='')
    print()

#while
'''
1. 초기식
while 2.조건식:
    code...
    3. 증가식
'''
#while 조건식이 참인동안 반복하는 반복문
#프로그램 종료 조건 필수

#실습1. continue를 이용하여 1부터 10까지 정수중 홀수만 출력하기
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numbers:
    if (i % 2) == 0:
        continue
    else:
        print(i, end = ' ')
#############
i = 0
while i < 10:
    i += 1
    if (i % 2)== 0:
        continue
    print(i, end = ' ')


#실습2. break를 이용하여 'shall we close? (y/n)' 문구에 y를 입력해야
#반복문을 탈출하고 'The end'를 출력하는 프로그램 작성

#실습3. 정수를 입력받아 그 정수가 몇자릿수 숫자인지 알아내는 프로그램 작성

n = int(input())
cnt = 0
while n > 0:
    cnt += 1
    n //= 10
print(cnt)

#list comprehension
#실습 1
import math
numbers = [1, 4, 9, 16, 25]

sqrt_numbers = []
for number in numbers:
    sqrt_numbers.append(int(math.sqrt(number)))
#list comprehension
sqrt_numbers2 = [int(math.sqrt(number)) for number in numbers ]

print(sqrt_numbers)
print(sqrt_numbers2)

#실습 2: if 추가 짝수만 추가하기
import math
numbers = [1, 4, 9, 16, 25]

sqrt_numbers = []
for number in numbers:
    if number % 2 ==0: #짝수 조건문 추가
        sqrt_numbers.append(int(math.sqrt(number)))
#list comprehension은 if문은 오른쪽으로
sqrt_numbers2 = [int(math.sqrt(number)) for number in numbers if number%2==0 ]

print(sqrt_numbers)
print(sqrt_numbers2)