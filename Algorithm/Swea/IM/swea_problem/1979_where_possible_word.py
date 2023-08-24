T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_t = [list(item) for item in zip(*arr)]

    result = 0
    for i in range(N):
        count = 0
        for j in range(N):
            if arr[i][j] == 1:
                count += 1
            if arr[i][j] == 0:
                count = 0
            # if 0<= j+1 <N:
            if count == K and (j == (N-1) or arr[i][j+1] == 0) :
                result += 1
                count = 0
    for i in range(N):
        count = 0
        for j in range(N):
            if arr_t[i][j] == 1:
                count += 1
            if arr_t[i][j] == 0:
                count = 0

            if count == K and (j == (N-1) or arr_t[i][j+1] == 0) :
                result += 1
    print(f'#{tc} {result}')

################
# T= int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     arr_t = [list(item) for item in zip(*arr)]
#     result = 0
#     for i in range(N):
#         for j in range(0, N-K+1):
#             if arr[i][j] == 1:
#                 if 0<= j+K <= N or (j+K+1 <= N and arr[i][j+K+1] == 0):
#                     if arr[i][j:j+K] == [1] * K:
#                         result += 1
#     print(result)