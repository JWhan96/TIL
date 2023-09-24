# def f(i, N):
#     if i == N: # 순열 완성
#         print(p)
#         return
#     else: # card[i]에 들어갈 숫자를 결정
#         for j in range(N):
#             if used[j] == 0: # 아직 사용되기 전이라면
#                 p[i] = card[j]
#                 used[j] = 1
#                 f(i+1, N)
#                 used[j] = 0

# N = 5
# card = [1, 2, 3, 4, 5]
# used = [0] * N #사용한 카드인지 표시하는 리스트
# p = [0] * N
# f(0, N)
def f(i, N):
    if i == N: # 순열 완성
        print(p)
        return
    else:
        for j in range(N):
            if used[j] == 0:
                # 첫 번째 요소가 1이 아닌 경우에는 더 이상 진행하지 않음
                if i == 0 and card[j] != 1:
                    continue

                p[i] = card[j]
                used[j] = 1
                f(i+1, N)
                used[j] = 0

N = 3
card = [1, 2, 3]
used = [0] * N # 사용한 카드인지 표시하는 리스트
p = [0] * N
f(0, N)
#이 코드에서 첫 번째 요소가 1이 아닌 경우, continue 문을 사용하여 더 이상 진행하지 않습니다. 이렇게 하면 첫 번째 요소가 1이 아닌 순열을 생성하지 않고 건너뛰어서 시간을 절약할 수 있습니다.





