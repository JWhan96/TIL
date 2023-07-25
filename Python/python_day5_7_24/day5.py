#sort 메서드
# print(numbers.sort()) #None

numbers = [3, 2, 1]
#sorted 함수
print(sorted(numbers))

list1= numbers
#2. 슬라이싱
list2 = numbers[:]
numbers[0] = 100

print(list1)
print(list2)