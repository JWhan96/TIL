T = int(input())
for tc in range(1, T+1):
    N, P = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

def bomb(y, x):
    direct = [(0,1), (0,-1), (1, 0), (-1, 0)]
    for i in range(N):
        for j in range(N):