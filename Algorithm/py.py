from itertools import permutations
# 7개의 정수를 입력
N, M = map(int, input().split())
numbers = list(map(int, input().strip().split()))

# 절대값으로 바꾸고 원래 값과 함께 튜플로 저장
abs_origin = [(abs(num), num) for num in numbers]

# 내림차순 정렬
sorted_origin = sorted(abs_origin, key=lambda x: x[0], reverse=True)

#원래의 값으로 다시 리스트를 구성
result = [num[1] for num in sorted_origin]

# print(result)  # 결과 출력

def Negative(result):
    for i in result:
        if i < 0:
            return True
    return False

check = list(permutations(result, M))

flag = 0
def Check():

    global flag
    if Negative(result):
        for i in check:
            gop = 1
            for j in i:
                gop *= j
                if gop < 0:
                    # print(gop)
                    flag = 1
                    break

            if flag == 1:
                break
    else:
        i = []
        for k in range(N-1, N-M-1, -1):
            i.append(result[k])
        else:
            return i

    return i
result1 = Check()
print(*sorted(result1))