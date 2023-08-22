T = int(input())
for tc in range(1, T+1):
    N = int(input())
    town = [list(map(int, input().split())) for _ in range(N+1)]


    #중계기 위치
    y, x = 0, 0
    for i in range(N+1):
        for j in range(N+1):
            if town[i][j] == 2:
                y, x = i, j
    # 집들의 위치
    home = []
    for i in range(N + 1):
        for j in range(N + 1):
            if town[i][j] == 1:
                home.append((i, j))
    # 거리 계산
    d_lst = []
    for h in home:
        D = abs(h[0] - y) **2 + abs(h[1] - x) **2
        d_lst.append(D)
    R = 1
    while R**2 < max(d_lst): # D**2 <=R : 통신범위에 포함
        R += 1

    print(f'#{tc} {R}')