# from collections import deque
# from pprint import pprint
#
# direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#
#
# def BFS(y, x):
#
#     queue = deque()
#     queue.append((y, x)) # 시작 위치 큐에 추가
#     visited = [[0] * M for _ in range(N)]
#     visited[y][x] = 1 # 시작위치 방문 표시
#
#     while queue:
#         # pprint(visited)
#         cy, cx = queue.popleft()
#
#
#         for dy, dx in direction:
#             ny = cy + dy
#             nx = cx + dx
#             if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0: #범위이내
#                 if arr[ny][nx] == 'L':
#                     visited[ny][nx] = visited[cy][cx] + 1 # 거리갱신
#                     queue.append((ny, nx)) #큐에 추가
#                 if visited[ny][nx] > visited[cy][cx] + 1:
#                     visited[ny][nx] = visited[cy][cx] + 1
#     return 0 # 경로없으면 0반환
#
# def Check(arr):
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == 'W':
#                 result.append((i, j))
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M= map(int, input().split())
#     result = []
#     arr = [list(map(str, input())) for _ in range(N)]
#     # start = (Check(arr))
#
#     # (BFS(start[0], start[1]))
#
#     print(arr)
#     # print(f'#{tc} {result}')
from collections import deque
from pprint import pprint




#
# def Check(arr):
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == 'W':
#                 result.append((i, j))


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    result = []
    arr = [list(map(str, input())) for _ in range(N)]
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                y, x = i, j
                queue = deque()
                queue.append((y, x))  # 시작 위치 큐에 추가

                 # 시작위치 방문 표시

                while queue:
                    # pprint(visited)

                    cy, cx = queue.popleft()

                    if visited[cy][cx] == -1:
                        break
                    visited[y][x] = -1
                    for dy, dx in direction:
                        ny = cy + dy
                        nx = cx + dx
                        if 0 <= ny < N and 0 <= nx < M and (len(visited[ny][nx]) != len(visited[cy][cx])):  # 범위이내
                            if arr[ny][nx] == 'L':
                                if visited[cy][cx][0kk] != -1:
                                    visited[ny][nx] = visited[cy][cx] + 1  # 거리갱신
                                    queue.append((ny, nx))  # 큐에 추가
                                else:
                                    visited[ny][nx] = 1  # 거리갱신
                                    queue.append((ny, nx))
                            if visited[ny][nx] > visited[cy][cx] + 1 and visited[cy][cx] != -1:
                                visited[ny][nx] = visited[cy][cx] + 1

    result = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] != -1:
                result += visited[i][j]

    print(result)
    #
    # # start = (Check(arr))
    #
    # # (BFS(start[0], start[1]))
    #
    # print(arr)
    # print(f'#{tc} {result}')