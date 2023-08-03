# red = 1
# blue = 2
T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    board = [[0] * 10 for _ in range(10)]
    cnt = 0
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                if board[r][c] == 0:
                    board[r][c] = color
                elif board[r][c] != color:
                    cnt += 1
                    board[r][c] = 3
    print(f'#{testcase} {cnt}')