# + 와 - 기호가 들어있는 수식을 입력받고 자동으로 계산해주는 프로그램을 작성
# 힌트
# parsing을 하기위한 메서드가 불충분하다면 필요한 함수를 직접 구현하는 것이 좋다
# 조건
# 1. 괄호는 없다
# 2. 첫 번째수는 양수 또는 음수가 될 수 있다
# 3. +와 - 이외 문자는 입력 x
# 4. 띄어쓰기 없이 입력
# 5. 문자열 길이 최대값 :1000
# 6. 최종 결과는 음수가 될 수 있다.
# 7. 첫번째 수가 양수라면 + 기호가 생략

# 입력
# 첫번쨰 줄에 다항식에 해당하는 문자열이 주어짐
# 출력
# 다항식을 연산한 결과 출력
'''
예시 1
100+100-50+30

출력
180
'''
####어떻게 나눌것인가 고민해보기 숫자와 문자열
# arr = list((input()))
# count = [0] * len(arr)
# list1 = []
#
# for i in range(len(arr)):
#     try:
#         number = int(arr[i])
#         list1.append(number)
#         count[i] += 1
#     except:
#         list1.append(arr[i])
#
# print(list1, count)
# result_list = []
# for i in range(0, len(count)):
#     if count[i] == 1 and count[i+1] == 1:
#         list1[i] = (list1[i] + list1[i+1])
# print(list1)
# print(result_list)
#

############
#메서드 이용
# print(eval(input()))

### 다른 방법
###첫번째가 음수일경우
# ex = input()
# if ex[0] == '-':
#     ex = '0' + ex
#
# print(ex)
# word = ex.split('+')
# ans = 0
# for w in word:
#     #뺄셈 기호를 기준으로 분리
#     print(w)
#     w = w.split('-')
#     #첫번째 요소는 더해줄 값
#     print(w)
#     inner_ans = int(w[0])
#     for i in range(1, len(w)):
#         inner_ans -= int(w[i])
#     #이 부분의 결과의 전체 합계
#     ans += inner_ans
# print(ans)

###
def par_sum(st):
    d=1
    if (st[0] != '-'):
        st1 = '+' + st
    else:
        st1 = st

    lst = []

    k = 0
    for i in range(1, len(st1)):
        if (not st1[i].isdigit()):
            lst.append(st1[k:i])
            k = i

    lst.append(st1[k:])

    s = 0
    for i in lst:
        if (i[0] == '+'):
            s += int(i[1:])

        if (i[0] == '-'):
            s -= int(i[1:])

    return s
st = input()
result = par_sum(st)
print(result)
