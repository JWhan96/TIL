'''
#### 폭탄 문제
N x M의 격자점 공간에 K화력의 폭탄들이 설치 되어 있습니다. N은 세로크기이며M은 가로크기입니다
여러개의 폭탄들이 동시에 터진다고 할 때 , 터지고 난후의 모양 프로그램
폭탄은 모두 동시에 상화좌우, 각각K칸으로 퍼짐 벽이있는곳 폭발 차단
k=1
0#@#@        0#%#%
0#0#0   ->   0#%#%
00000        00000

k=2
0#0#0        %#%#0
0#0#0    ->  %#%#0
@0@00        %%%%%

첫줄에는 세로(N), 가로(M)크기 입력 (1<=N<=20)
다음 줄 화력 K  (1<=K<=10)

입력예시 1
3 5
2
_#_#@
_#_#@
@___#

출력 예시
%#_#%
%#_#%
%%%_#

입력 예시2
3 5
2
_#_#_
_#_#_
@_@__

출력
%#%#_
%#%#_
%%%%%
'''

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
