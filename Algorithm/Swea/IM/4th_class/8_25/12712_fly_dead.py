def spray(y, x):
    # 상하좌우 4, 대각선 4
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    s1 = s2 = arr[y][x]
    for i in range(4):
        for j in range(1, M):
            dy = y + dir[i][0] * j
            dx = x + dir[i][1] * j
            if 0 <= dy < N and 0 <= dx < N:
                s1 += arr[dy][dx]
    for i in range(4, 8):
        for j in range(1, M):
            dy = y + dir[i][0] * j
            dx = x + dir[i][1] * j
            if 0 <= dy < N and 0 <= dx < N:
                s2 += arr[dy][dx]
    return max(s1, s2)

T = int(input())
for tc in range(1, T+1):
    N, M= map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    for i in range(N):
        for j in range(N):
            s = spray(i, j)
            if s > max_v: #최대 파리수 업데이트
                max_v = s
    print(f"#{tc} {max_v}")

