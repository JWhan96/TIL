# 함수 정의, 함수 선언
'''
def 함수명(매개변수):
    code....     함수바디     
    code....     함수바디
    return 반환값

'''
#함수호출

'''
함수명(함수인자)
'''

# 매개변수는 있을 수도 있고 없을 수도 있다.
# 반환값은 있을 수도 있고 없을 ㅁ수도 있다. 
# ---->총 4가지 유형의 함수가 존재\

def get_sum(num1, num2):
    return num1 + num2

num1 = 5
num2 = 3
result = get_sum(num1, num2)
print(result)

#1 매개변수가 없는 함수로 변형
def get_sum():
    num1 = 5
    num2 = 3
    return num1 + num2

result = get_sum
print(result)

#2. return반환값이 없는 함수로 변형
def get_sum(num1, num2):
    result = num1 + num2
    print(result)

num1 = 5
num2 = 3
get_sum(num1, num2)

# map함수를 사용하여 numbers 리스트의 각 요소가 제곱된 값들로 이루어진 새로운 리스트
numbers = [1, 2, 3, 4, 5]

result = (map(lambda x: x ** 2 , numbers))
print(result)