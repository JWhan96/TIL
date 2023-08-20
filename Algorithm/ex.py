from pprint import pprint
N, M = map(int, input().split())
K = int(input())
arr = [list(input()) for _ in range(N)]

direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for i in range(N):  #행
    for j in range(M): #열
        if arr[i][j] == '@':
            for ny, nx in direct:  # 방향 지정
                for k in range(1, K+1): #폭발 범위

                    dy = i + (k*ny)
                    dx = j + (k*nx)
                    if 0<= dy <N and 0<= dx <M:
                        if arr[dy][dx] == '_':
                            arr[dy][dx] = '%'
                        elif arr[dy][dx] == '#':
                            break
            arr[i][j] = '%'

pprint(arr)