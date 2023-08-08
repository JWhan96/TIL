#중괄호{}, 대괄호[]가 존재
# []대괄호 안에 있는 숫자는 +
# {}중괄호 안에 있는 숫자는 *

#방법1: find쓰기, 방법2: 안쓰기
# ABC123[10]B{3}AT[20][10]BB{2}Q
#1. 0 + [10] = 10
#2. 10 * {3} = 30
#3. 30 + [20] = 50
#4. 50 + [10] = 60
#5. 60 * {2} = 120

#세부조건
# 1. 연산의 결과에 해당하는 수는 1~10000
# 2. 숫자는 모두 양수
# 3. 괄호가 부정확한 데이터는 입력 X
# 4. 괄호 안에는 모두 숫자로 구성
#
# arr = list(input())
#
# for i in range(len(arr)):
#     if arr[i] == '[':
#         print(i)
#         for j in range(i+1, len(arr)):
#             if arr[j] == ']':
#                 print(j)
#                 break
# for i in range(len(arr)):
#     if arr[i] == '{':
#         print(i)
#         for j in range(i+1, len(arr)):
#             if arr[j] == '}':
#                 print(j)
#                 break

word = input()
result = 0
for i in range(len(word)):
    temp = ''
    #현재 검사할 문자의 다음 인덱스
    index = i + 1
    if word[i] == '[':
        while word[index] != ']':
            #임시 문자열 temp변수에 현재 문자 추가
            temp += word[index]
            index += 1
            print(temp)
        result += int(temp)
        print(temp)
    elif word[i] == '{':
        while word[index] != '}':
            temp += word[index]
            index += 1
        result *= int(temp)
print(result)
#
# a = 'ab'
# a += 'c'
# print(a)