def room():
    # global cnt
    visited = [[0]*N for _ in range(N)]
    cnt = 1
    while stack:
        y, x = stack.pop()
        visited[y][x] = 1
        for i in range(4):  # 4방향 탐색
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx]==0:
                if arr[ny][nx] == (arr[y][x] + 1):
                    # 갈 수 있는 곳을 모두 stack에 추가
                    stack.append((ny, nx))
                    cnt += 1



    return cnt


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dy = [0, 1, 0, -1]  # 세로
    dx = [1, 0, -1, 0]  # 가로
       # 우 하 좌 상
    value = 0
    index = float('inf')
    result = []
    for y in range(N):
        for x in range(N):
            # 시작점 찾기
            stack = [(y, x)]  # 시작점 스택에 추가
            cnt1 = room()
            if cnt1 > value:
                value = cnt1
                index = arr[y][x]
            elif cnt1 == value and arr[y][x] < index:
                index = arr[y][x]

    print(f'#{tc}', index, value)

####원석님 코드
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    max_rooms = 0
    ans = (A[0][0], 0)
    total_visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not total_visited[i][j]:
                queue = [[i, j, 1]]
                directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                max_aij = 0
                while queue:
                    now_i, now_j, rooms = queue.pop(0)
                    total_visited[now_i][now_j] = 1
                    max_aij = max(max_aij, rooms)
                    for di, dj in directions:
                        if 0 <= now_i + di < N and 0 <= now_j + dj < N:
                            if A[now_i + di][now_j + dj] - A[now_i][now_j] == 1:
                                queue.append([now_i + di, now_j + dj, rooms + 1])

                if max_rooms < max_aij:
                    ans = (A[i][j], max_aij)
                    max_rooms = max_aij
                elif max_rooms == max_aij:
                    if ans[0] > A[i][j]:
                        ans = (A[i][j], max_aij)
    print(f"#{tc}", *ans)

### 강사님 코드
direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0] * (N*N+1)
    for i in range(N):
        for j in range(N):
            for r, c in direct:
                if 0<= i+r <N and 0 <= j+c < N and arr[i][j] +1 == arr[i+r][j+c]:
                    v[arr[i][j]]= 1#연속된 숫자임을 표시
    start, cnt, temp = 0, 1, 1
    for i in range(len(v)-1, -1, -1):
        if v[i] ==1:
            temp += 1
        else: #연속이 끊긴 경우
            if cnt<= temp:
                cnt = temp
                start = i+1 #시작점 갱신
#             temp = 1 # 연속카운트 초기화
#     print(f'#{tc} {start} {cnt}')

