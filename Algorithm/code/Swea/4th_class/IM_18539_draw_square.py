# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     board = [list(map(int, input().split())) for _ in range(N)]
#     maxv, tcnt = 1, 0
#     for sc in range(N):
#         for sr in range(N):
#             cur = board[sc][sr]
#             for i in range(sc, N):
#                 for j in range(sr, N):
#                     if board[i][j] == cur:
#                         square = (i - sc + 1) * (j - sr + 1)
#                         if square > maxv:
#                             maxv = square
#                             tcnt = 1
#                         elif square == maxv:
#                             tcnt += 1
#
#     print(f'#{tc} {tcnt}')

#################
