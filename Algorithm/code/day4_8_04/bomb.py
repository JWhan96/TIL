from pprint import pprint

N, M = map(int, input().split())
K = int(input())
arr = [list(input().strip()) for _ in range(N)]

# def expl(y, x):
direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for k in range(N):
    for h in range(M):

        if arr[k][h] == '@':

            for i, j in direct:
                for u in range(1, K + 1):
                    dir_y = k + i*u
                    dir_x = h + j*u

                    if 0 <= dir_y < N and 0 <= dir_x < M:

                        if arr[dir_y][dir_x] == '#':
                            break
                        #그냥 이렇게 넣으면 폭탄이 바뀌어 버리면 안터진다.
                        # arr[dir_y][dir_x] = '%'

                        #그래서 터질 때 _ 이구간만 터지게
                        if arr[dir_y][dir_x] == '_':
                            arr[dir_y][dir_x] = '%'
            arr[k][h] = '%'


pprint(arr)

###강사님 코드
# N, M = map(int, input().split())
# K = int(input())
# arr = [list(input()) for _ in range(N)]
# directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
#
# #NxM 행렬
# for i in range(N):
#     for j in range(M):
#         # 폭탄이 설치되어 있다면
#         if arr[i][j] == '@':
#             # 폭탄은 상, 하, 좌, 우 방향으로 폭발
#             for dy, dx in directions:
#                 # 폭탄이 터지는 화력
#                 for k in range(1, K + 1):
#                     ny, nx = i + (k * dy), j + (k * dx)
#                     if 0 <= ny < N and 0 <= nx < M:
#                         if arr[ny][nx] == '_':
#                             arr[ny][nx] = '%'
#                         if arr[ny][nx] == '#':
#                             break
#             arr[i][j] = '%'
# for row in arr:
#     print(*row, sep='')
