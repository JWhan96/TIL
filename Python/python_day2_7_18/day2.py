##Numeric Type##

# 진법 변경
print(0b1100)
print(bin(12))
print(0o14)
print(oct(12))
print(0xc)
print(hex(12))

# 메모리 용량이 한정돼 있고 저장하는 용량이 제한
#가까운 값으로 출력
print(2/3)
print(5/3)

#10진수의 0.1은 2진수로 표현하면 무한대 숫자로 표현
#근삿값만 표시하게 되고, 예상치 못한 결과가 생긴다
#이를 "floating point rounding error"라고 칭함
a = 3.2 - 3.1
b = 1.2 - 1.1
#임의의 작은 수 활용
print(abs(a-b) <= 1e-10) #True
#2. math모듈 사용
import math
print(math.isclose(a,b)) #True

#지수(제곱수)표현 10^
print(314e-2) #3.14
print(314e2)  #31400.0

###########
##Sequence Types##(ex:str, list, tuple, range)
#특징
#1. 순서 : 값들이 순서대로 저장 (정렬x)
#2. 인덱싱 : 고유한 인덱스(번호)를 가지고 있으며 특정위치의 값을 선택하거나 수정가능
#3. 슬라이싱 : 인덱스 범위를 조절, 부분적인 값 추출가능
#4. 길이 : len()함수를 사용하여 저장된 값의 개수(길이)를 구할 수 있음
#5. 반복 : 반복문 사용, 저장된 값들을 반복 처리 가능

#str(문자열): 문자들의 순서가 있는 변경 불가능 시퀀스 자료형
#'' 또는 ""로 감싸서 표현

#작은따옴표 쓰고싶으면 큰따옴표로, 큰따옴표쓰고싶으면 작은 따옴표로
print('여기서 "큰 따옴표"사용')
print("여기서 '작은 따옴표'사용")

#Escape sequence
#역슬래쉬(\)뒤에 특수문자가 와서 특수한 기능을 하는 문자 조합
#사진 넣기########################

#String interpolation: 문자열 내에 변수나 표현식을 삽입하는 방법
#f-string
#'Debugging roaches 13 room'출력을 변수에 따라 삽입 하고 싶을 때
bugs = 'roaches'
counts = 13
area = 'room'
print(f'Debugging {bugs} {counts} {area}')
#다른 방법 2개
print('Debugging {} {} {}'.format(bugs, counts, area))
print('Debugging %s %d %s' % (bugs, counts, area))

#f-string 응용(advanced 검색해서 공부)
greeting = 'hi'
print(f'{greeting:^10}')#10칸중에 가운데 정렬
print(f'{greeting:>10}')#오른쪽 정렬
print(f'{3.141592:.2f}')#실수 반올림가능

##문자열의 시퀀스 특징
my_str = 'hello'
#1. 인덱싱
print(my_str[1]) #e
#2. 슬라이싱
print(my_str[2:4]) #ll
#3. 길이
print(len(my_str)) #5

##########################
#인덱스
#####사진######hello인덱스 음수까지나와있는거

#슬라이싱
#슬라이싱할떄 공백을 기준으로 생각하면 편하다(강의필기 참고)
my_str = 'hello'
print(f'{my_str[2:4]}') #2부터 4까지
print(f'{my_str[:4]}') #처음부터 4까지
print(f'{my_str[3:]}')  #3부터 끝까지
print(f'{my_str[0:5:2]}') #0부터 5까지 2칸씩띄기
print(f'{my_str[::-1]}') #문자열 뒤집기(-인덱스가 있어서 가능)

#문자열은 변경 불가
my_str = 'hello'

#TypeError: 'str' object does not support item assignment
my_str[1] = 'z' #불변이라 에러
#==>새로운 문자열을 배정해주는 방법으로 바꾼다

##리스트: 변경가능 시퀀스 자료
#0개이상(빈리스트가능) 객체 포함, 데이터 목록 저장
list1 = []
#[대괄호]로 표기
list2 = [1, 2, 3]
#어떤 자료형도 저장 가능
list3 = [1, 2, 3, 'python', ['hello', 'world', '!!!']]  

##시퀀스특징
###########예시########강의자료

#중첩된 리스트 접근
my_list = [1, 2, 3, 'python', ['hello', 'world', '!!!']] 
print()
###리스트의 할당
list1 = [1, 2, 3]
list2 = list1
list1[0] = 100
print(list2)  #[100, 2, 3] 이유는 리스트2는 리스트1의 칸 주소 메모리를 참조하는것이고
#리스트 1의 [0]은 1에서100으로 참조하기때문에 리스트1[0]의 값이 리스트2에도 적용
########### 파이썬 튜터사진 넣기#############가변형이라 그렇다.


##Tuple: 변경 불가능한 시퀀스 자료형
#0개 이상의 객체 포함, 데이터 목록 저장
tuple1 = ()
#(소괄호)로 표기
tuple2 = (1)  # type=int 연산으로 작용
tuple2 = (1,) # type=tuple
#데이터는 어떤 자료형도 저장 가능


#시퀀스 특징
############리스트에서 변환해서 적기

#튜플은 불변(변경 불가)
#여러 개의 값을 전달, 그룹화, 다중할당 등 '파이썬 내부 동작'에서 사용
#문제 푸는 데 직접적으로 이용할 일은 없다

##range: 연속된 정수 시퀀스를 생성하는 변경불가 자료형(반복문에서 주로 사용)
range1 = range(5)
range2 = range(1, 10)

print(range1) #range(0, 5)
print(range2) #range(1, 10)
#list형으로 변환하여 데이터 확인 가능
print(list(range1)) #[0, 1, 2, 3, 4]
print(list(range2)) #[1, 2, 3, 4, 5, 6, 7, 8, 9]


#####Non Sequence Types

##dictionary: key와 value 쌍으로 이루어진 순서와 중복x, 변경가능 자료형
#key를 통해 value에 접근
#key는 변경불가 자료만 가능(str, int, float, tuple, range ...)
#value는 모든 자료형 가능
#{중괄호}로 표시   {키:밸류, 키:밸류}
dict = {}


##set: 순서와 중복x, 변경가능 자료형
#수학에서의 집합과 동일한 연산처리 가능
#{중괄호}로 표기
set1 = set() #dict에 밀려서 빈 세트는 이렇게 생성
set2 = {1, 3, 2}
set3 = {1 ,1 ,1}

print(set1)  #set()
print(set2)  #{1, 2, 3}  순서가 없어서(인덱스 x) 이렇게 출력
print(set3)  #{1} 중복이 없어서 이렇게 출력

#세트의 집합 연산
set1 = {1, 2, 3}
set2 = {3, 6, 9}
#합집합
print(set1 | set2) #{1, 2, 3, 6, 9}
#차집합
print(set1 - set2) #{1, 2}
#교집합
print(set1 & set2) #{3}


###Other Types

#None: "값이 없음"을 표현하는 자료형


#Boolean: 참(True), 거짓(False)를 표현하는 자료형
#비교/논리 연산의 평가결과로 사용
#주로 조건/반복문과 함께 사용
#정수 -> False:0
#실수 -> False:0.0
#문자열' '(공백) ->

a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))
print(id(b))
print(a == b)  #동등성(구성 요소들이 같은지)
print(a is b)  #식별성(주소가 같은지, 객체(list, str, dict등등) 비교)




##Collection: 여러개의 항목 또는 요소를 담는 자료 구조(str, list, tuple, set, dict)
#정렬여부X -> 나열,순서 여부(표 바꾸기)
########표삽입###########


##암시적 형변환
#Boolean 타입과 Numeric type만 가능
print(True + 3)  #4
print(3 + 3.0)  #6.0

##명시적 형변환
#str -> int  형식에 맞는 숫자만 가능
#int -> str  모두 가능
print(str(1) + '등') #  1등
print(int(3.5))  #3   int로 형변환을 하면 버림으로 취급
 
#산술연산자

#복합연산자

#비교연산자 

#논리연산자


#단축평가
vowels = 'aeiou'

print(('a' and 'b') in vowels) #b가 출력 되어서 False
print(('b' and 'a') in vowels) #a가 출력 되어서 True

print(3 and 5) #5
print(0 and 3) #0
print(3 and 0) #0 
print(0 and 0) #0

print(3 or 5)  #3
print(0 or 3)  #3
print(3 or 0)  #3
print(0 or 0)  #0

#시퀀스형 연산자
# + : 결합연산자
# * : 반복연산자 /문자열 * 문자열 불가


