# 세트 가변형 비시퀀스 -> 중복을 허용하지 않는다 -> 집합과 같은 특징

list1 = [1, 2, 3]
list2 = [4, 5, 6, 7, 8, 9]
set1 = set(list1)
set2 = set(list2)

#1. set1에 4추가
set1.add(4)
print(set1)

#2. set1에 [5, 6, 7]추가
set1.update([5, 6, 7])
print(set1)
#3. set1에서 7제거(2가지 방법)
set1.remove(7)
print(set1)
set1 = {1, 2, 3, 4, 5, 6, 7}
set1.discard(7)
print(set1)
#4. set1 차집합 set2 출력(2가지 방법)
print(set1 - set2)
print(set1.difference(set2))
#5. set1 교집합 set2 출력(2가지 방법)
print(set1 - set2)
print(set1.intersection(set2))
#6. set1 합집합 set2 출력(2가지 방법)
print(set1 - set2)
print(set1.union(set2))

#set1.pop(): 주소값이 작은 것부터 제거
set1 = {1, 2, 3, 'a', 4, 5, 6}
print(id(1))
print(id(2))
print(id(3))
print(id(4))
print(id('a'))
print(set1.pop())
print(set1.pop())
print(set1.pop())
print(set1)

#dictionary 메서드
#영한사전 dict 실습
# plus : 더하기 장점
# minus : 빼기 적자
# multiply : 곱하기 다양하게
# division : 나누기 분열
ek_dict = {
    'plus' : ['더하기', '장점'],
    'minus' : ['빼기', '적자'], 
    'multiply' : ['곱하기', '다양하게'],
    'division' : ['나누기', '분열']
}
#1. 영어 단어를 입력하면 단어의 뜻을 보여주는 프로그램(2가지 방법)
print(ek_dict['plus'])
print(ek_dict.get('plus'))
print(ek_dict.setdefault('plus'))

#2. 영한사전에서 단어들의 목록을 출력
ek_keys = ek_dict.keys()
print(ek_keys)
for ek_key in ek_keys:
    print(ek_key) 

#3. 다음 단어와 뜻을 추가하고, 사전에 있는 모든 단어와 뜻을 출력(3가지 방법)
# square : 제곱, 사각형
#1)
print(ek_dict.setdefault('square' , ['제곱', '사각형'])) #['제곱', '사각형']
print(ek_dict)
#2)
ek_dict.update(square = ['제곱', '사각형']) #None이기 때문에 새로 추가
print(ek_dict)
#3)
# ek_dict['square'] = ['제곱', '사각형']
# print(ek_dict)
### 단어 뜻 출력
print(ek_dict.items())

#4. 입력받은 단어와 뜻을 삭제하는 프로그램 작성(2가지 방법)
ek_dict.pop('square')
print(ek_dict)
del ek_dict['plus']
print(ek_dict)