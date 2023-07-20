# 문자열 ' '  : 불변 시퀀스 자료형 -> 알고리즘 IM형 문다열 파싱
# 리스트 [ ]  : 가변 시퀀스 자료형 -> 알고리즘 IM형 방향배열 등.. A형 DFS, BFS
# 튜플   ( )  : 불변 시퀀스 자료형
# 딕셔너리{:} : 가변 비시퀀스 자료형 -> DB의 json 형식과 비슷
# 세트   { }  : 가변 비시퀀스 자료형 -> 중복 허용 X -> 집합

decimal = 10
#1. 2진수로 출력
print(bin(decimal))  #binary / 0b1010
print(bin(decimal)[2:]) #0b생략을 위해 슬라이싱
#2. 8진수로 출력
print(oct(decimal))  #octal / 0o12
#3. 16진수로 출력
print(hex(decimal))  #hexa / 0xa


a = 3.2 - 3.1
b = 1.2 - 1.1
# 부동 소수점 값을 출력 할 때 f-string을 활용하여 부동소수점의 정확도를 제어 가능
print(f'a의 값은: {a}, b의 값은: {b}')         #제어 X : a의 값은: 0.10000000000000009, b의 값은: 0.09999999999999987
print(f'a의 값은: {a:.1f}, b의 값은: {b:.1f}') #제어 O : a의 값은: 0.1, b의 값은: 0.1

print(314e-2)
#산술연산자를 사용하여 표현식 변환
print(314 * 10 ** -2)

greeting = 'hi'
print(f'{greeting:>10}') #오른쪽 정렬 /         hi
print(f'{greeting:^10}') #가운데 정렬 /     hi
print(f'{greeting:<10}') #왼쪽 정렬   / hi

print('####################')
########IM형 문자열파싱????그게 뭐지###############
# ##alt누른 상태로 클릭하면 여러 곳 클릭 가능-> 한번에 같은 단어 여러번 가능
greeting = 'Hello world'
#1. 인덱싱 -> 알파벳 w를 출력해 보세요.
print(greeting[6])
#2-1 슬라이싱 -> Hello를 출력해 보세요.
print(greeting[:5])
#2-2 슬라이싱 -> world를 출력해 보세요.
print(greeting[6:])
#2-3 슬라이싱 -> 거꾸로 출력해 보세요.
print(greeting[::-1])
#3. 내장함수를 사용해서 문자열의 길이를 출력해 보세요.
print(len(greeting)) #공백도 index에 포함
#4. for문을 활용하여 hello world를 출력해 보세요.(2가지 방법)
for i in greeting:
    print(i, end = '')
print()

for i in range(len(greeting)):
    print(greeting[i], end = '')
print()
#위랑 동일
# for i in range(11):
#     print(greeting[i], end = '')
# print()

##행과 열로 구분이 가도록 작성하면 좋다.
array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#1 인덱싱 하여 3을 출력해 보세요.
print(array[0][2])  #0행 2열
#2.언덱싱 하여 7을 출력해 보세요.
print(array[2][0])  #2행 0열


#2차원 리스트를 입력받는 방법
rows = int(input('행의 개수를 입력하세요.'))
matrix = []

# for i in range(rows):
#     row = list(map(int, input().split()))
#     matrix.append(row)   ##리스트에 추가하는 내장함수
matrix = [list(map(int, input().split())) for _ in range(rows)]
for row in matrix:
    print(row)
print(matrix)
############# 

#튜플을 사용하는 예시 : 방향배열

def move_around(position):
    x, y = position
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] #상하좌우
    directions_2 = [(-1, 1), (1, -1), (1, 1), (-1, -1)]

# range -> 주로 반복문과 함께 쓰인다
range(5)
#range(end) : 0부터 end-1까지 1만큼 증가
for i in range(5):
    break
range(2, 5) # 2부터 5-1까지 1씩 증가

range(1, 10 ,2)
#range(start, end, step)
#start < end : start부터 end -1 까지 step만큼씩 증가
#start > end : start부터 end +1 까지 step만큼 씩 감소

for i in range(10, 0 -1):
    print(i)

my_dict = {
'a1' : {'b1' : 1, 'b2' : 2, 'b3' : 3},
'a2' : {'b1' : 4, 'b2' : 5, 'b3' : 6},
'a3' : {'b1' : 7, 'b2' : 8, 'b3' : 9}
}
# value 5를 출력
print(my_dict['a2']['b2'])
print(my_dict.get('a2').get('b2'))


set_1 = {1, 2, 3, 4, 5, 6}
set_2 = {4, 5, 6, 7, 8, 9}
#합집합
print(set_1 | set_2)
#차집합
print(set_1 - set_2)
#교집합
print(set_1 & set_2)



#세트의 사용 예시 -> 로또 번호 추첨
import random


#####1. 6번만 반복, 세트에서 중복이 안되므로 중복된 숫자가 나온다면 세트의 len이 6이 아닐경우가 있다.
#6개의 숫자를 뽑아야 하므로 틀린 방법. 
number_set = set()
for i in range(6):
    number = random.randint(1, 45)
    number_set.add(number)
print(number_set)
number_list = list(number_set)
number_list.sort()
print(number_list)

#####2. set는 중복이 안되고 6개의 세트가 채워질때까지 반복
#고쳐진 방법: 리스트로 받게 되면 중복이 되므로 세트로 먼저 받은 후 리스트로 순서정렬
#            중복된게 나오면 세트에 저장이 안되고 6개채워질때까지 뽑아야하므로 while을 사용하여야 한다.
lotto_set = set()
while len(lotto_set) < 6:
    number = random.randint(1, 6)
    lotto_set.add(number)

lotto_list = list(lotto_set)
lotto_list.sort()
print(lotto_list)

#복합연산자 예시
numbers = [1, 2, 3, 4, 5]

total = 0

for num in numbers:
    total += num

print(total)