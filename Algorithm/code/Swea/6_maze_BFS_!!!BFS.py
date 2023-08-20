from collections import deque
from pprint import pprint

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def BFS(y, x):

    queue = deque()
    queue.append((y, x)) # 시작 위치 큐에 추가
    visited = [[0] * N for _ in range(N)]
    visited[y][x] = 1 # 시작위치 방문 표시

    while queue:
        # pprint(visited)
        cy, cx = queue.popleft()

        if arr[cy][cx] == 3: #도착위치면 거리반환
            return visited[cy][cx] - 2 #시작과 끝을 제외
        for dy, dx in direction:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < N and 0 <= nx < N: #범위이내
                if arr[ny][nx] != 1 and visited[ny][nx] == 0: #벽이 아니고 방문안한 경우
                    visited[ny][nx] = visited[cy][cx] + 1 # 거리갱신
                    queue.append((ny, nx)) #큐에 추가

    return 0 # 경로없으면 0반환

def Check(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input())) for _ in range(N)]
    start = (Check(arr))
    result = (BFS(start[0], start[1]))
    print(f'#{tc} {result}')