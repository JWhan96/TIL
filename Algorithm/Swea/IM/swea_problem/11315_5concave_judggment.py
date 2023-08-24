
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]  # '.' 'o'
    # arr_t = [list(item) for item in zip(*arr)]
    def cor():
        direct1 = [(0,1), (1,0), (1, 1), (1, -1)]
        # direct2 = [(1, 1), (1, -1)]
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 'o':
                    for ny, nx in direct1:
                        count = 0
                        for k in range(1, 5):
                            dy = i + (k*ny)
                            dx = j + (k*nx)
                            if 0<=dy<N and 0<=dx<N:
                                if arr[dy][dx] == 'o':
                                    count += 1
                            if count == 4:
                                return 'YES'
        return 'NO'
    result = cor()
    print(f'#{tc} {result}')