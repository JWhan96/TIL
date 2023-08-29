# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#     max_v = 0
#     sum_v = 0
#     lst = []
#     for i in range(M):
#         sum_v += arr[i]
#         max_v = sum_v
#     lst.append([0, 0+M-1])
#     for j in range(N-M):
#         sum_v -= arr[j]
#         sum_v += arr[j+M]
#         if sum_v > max_v:
#             max_v = sum_v
#             lst.pop()
#             lst.append([j+1, j+M])
#
#
#
#     print(f'#{tc}', *lst[0], f'{max_v}')
#

##############
T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    # 시작점 끝점 초기화
    start = 0
    end = m - 1
    # 공통 구간의 초기 합
    midsum = sum(arr[:end])
    # 변수 초기화
    ans = -999999
    s_index = 0
    e_index = 0
    while end < n:
        midsum += arr[end]  # 마지막 값 추가
        # 최대값 갱신
        if midsum > ans:
            ans = midsum
            s_index = start
            e_index = end
        midsum -= arr[start]  # 첫번째값지정
        start += 1
        end += 1
    print(f'#{tc} {s_index} {e_index} {ans}')