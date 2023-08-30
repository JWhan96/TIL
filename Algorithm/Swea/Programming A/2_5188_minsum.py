# direct = [(0, 1), (1, 0)]
# def dfs(y, x, sum_v): #x,y는 현재위치 , sum_v는 현재까지의 합계
#     global result
#     # 가지치기: 불필요한 경로를 차단 -> 조건에 맞지않으면 탐색 X
#     if sum_v >= result:
#         return
#     # 목표지점에 도착한 경우
#     if x == N-1 and y==N-1:
#         if sum_v < result:
#             result = sum_v
#     for dy, dx in direct:
#         ny = y + dy
#         nx = x + dx
#         if -1 < nx < N and -1 < ny< N:
#             dfs(ny, nx, sum_v + arr[ny][nx])
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split()))for _ in range(N)]
#     result = float('inf') #무한대 표현 , 음의 무한대 -float('inf')
#     #탐색
#     dfs(0, 0, arr[0][0])
#     print(f'#{tc} {result}')

#$######
direct = [(0, 1), (1, 0)]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = float('inf')

    stack = [(0, 0, arr[0][0])]  # (y, x, sum_v)를 스택에 넣어 사용

    while stack:
        y, x, sum_v = stack.pop()

        # 가지치기
        if sum_v >= result:
            continue

        # 목표지점에 도착한 경우
        if x == N-1 and y == N-1:
            if sum_v < result:
                result = sum_v
            continue

        for dy, dx in direct:
            ny = y + dy
            nx = x + dx
            if -1 < nx < N and -1 < ny < N:
                stack.append((ny, nx, sum_v + arr[ny][nx]))

    print(f'#{tc} {result}')






