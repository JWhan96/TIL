my_dict = {
            'name' : '진우'
            
}
print(my_dict['name'])
print(my_dict.get('name'))
# print(my_dict['age']) ##error
print(my_dict.get('age')) #None
print(my_dict.get('age', 'Unknown')) #Unknown
##키값 뽑아내기
person = {'name' : 'Alice', 'age' : 25}
print(person.keys()) #dict_keys(['name', 'age'])
for k in person.keys():
    print(k)
# name
# age

#밸류값 뽑아내기
print(person.values()) #dict_values(['Alice', 25])
for value in person.values():
    print(value)
# Alice
# 25

#키밸류 동시
print(person.items()) #dict_items([('name', 'Alice'), ('age', 25)])
for key, value in person.items(): 
    print(key, value)
# name Alice
# age 25

#pop
print(person.pop('age')) #25
print(person) #{'name': 'Alice'}
print(person.pop('country', None)) #.pop(key[,default]) 키가 없을 때 반환해주는 값 지정
# print(person.pop('country')) #없으면 error

person = {'name' : 'Alice', 'age' : 25}
## 키와 연결된 값을 반환, 없다면 추가까지(.get()은 None반환)
print(person.setdefault('country', 'Korea')) #Korea
print(person) #{'name': 'Alice', 'age': 25, 'country': 'Korea'}

#update([other])
#other 가 제공하는 키/값 쌍으로 딕셔너리 갱신, 기존 키를 덮어씀
#여러개 동시에도 가능
person = {'name' : 'Alice', 'age' : 25}
other_person = {'name' : 'Jane', 'gender' : 'Female'}
# 같은 키가 있다면 덮어쓴다
person.update(other_person)
print(person) #{'name': 'Jane', 'age': 25, 'gender': 'Female'}
# 직접 value값을 바꿀 수 있다
person.update(age = 50)
print(person) #{'name': 'Jane', 'age': 50, 'gender': 'Female'}
# 키/밸류쌍이 없다면 추가
person.update(country = 'Korea')
print(person) #{'name': 'Jane', 'age': 50, 'gender': 'Female', 'country':'Korea'}
# 키/밸류쌍 다른 방법
person.update({'countr' : 'Korea'})
print(person)


# 혈액형 인원수 세기
# 결과 => {'A' : 3, 'B': 3, 'O' : 3, 'AB' : 3}
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']

#1. []
new_dict = {}
# blood_types를 순회하면서
for blood_type in blood_types:
    #기존에 키가 이미 존재할 때
    if blood_type in new_dict:
        new_dict[blood_type] += 1
    #키가 처음 설정 될 때
    else : 
        new_dict[blood_type] = 1

print(new_dict)



#2. .get()
new_dict = {}
for blood_type in blood_types:

    new_dict[blood_type] = new_dict.get(blood_type, 0) + 1
print(new_dict)
#3. .setdefault()
new_dict = {}
for blood_type in blood_types:
    new_dict.setdefault(blood_type, 0)
    new_dict[blood_type] += 1
print(new_dict)

# 결과값 고민 #{'A': 0, 'B': 0, 'O': 0, 'AB': 0}
new_dict = {}
for blood_type in blood_types:
    new_dict.setdefault(blood_type, 0) + 1
    # new_dict[blood_type] += 1
print(new_dict)

#복사
a = [1, 2, 3]

#슬라이싱
b = a[:]
b[0] = 100
print(a, b) #[1, 2, 3] [100, 2, 3]

c = a.copy()
c[0] = 100
print(a, c) #[1, 2, 3] [100, 2, 3]

#얕은 복사의 한계
a = [1, 2, [1, 2]]
b = a[:]
b[2][0] = 999
print(a, b) #[1, 2, [999, 2]] [1, 2, [999, 2]]

a = [1, 2, [1, 2]]
c= a.copy()
c[2][0] = 999
c[1] = 30
print(a, c) #[1, 2, [999, 2]] [1, 30, [999, 2]]
#첫번째 인덱스까지는 복사가 되지만 더 안쪽 인덱스로 가면 같은 주소값을 
#바라보게 되어 일어나는 얕은 복사 

# 깊은 복사
import copy #카피관련

a = [1, 2, [1, 2]]
c= copy.deepcopy(a)
c[2][0] = 999
print(a, c) #[1, 2, [1, 2]] [1, 2, [999, 2]]