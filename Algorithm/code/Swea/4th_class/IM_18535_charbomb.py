T = int(input())
for tc in range(1, T+1):
    N, P = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    direct = [(0, 1),(0, -1),(1, 0),(-1, 0) ]
    max_v = 0
    for i in range(N):

        for j in range(N):
            sum_v = 0
            for p in range(1, P+1):
                for ny, nx in direct:
                    dy = i + (ny*p)
                    dx = j + (nx*p)
                    if 0<=dy<N and 0<=dx<N:
                        sum_v += arr[dy][dx]
            sum_v += arr[i][j]
            if max_v < sum_v:
                max_v = sum_v

    print(f'#{tc} {max_v}')
