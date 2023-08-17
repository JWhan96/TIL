#오목?
'''
4x5 사이즈의 맵(문자배열)준비, 모든칸은 언더바'_'로 채우기
폭탄을 투하할 좌표(Y,X) 두 곳을 입력받기
두 폭탄이 터진 후의 맵 출력
폭탄이 터지면 상 하 좌우 그리고 대각선 방향이 '#'으로 표시

폭탄이 (1, 1)그리고 (3, 3)좌표에 투하되었다면 (1, 1)주변으로 터지기
그 후 (3,3)에 터지면 없는 부분은 '#'이 없고 겹치는 부분이 있다면 그대로 유지
'''

'''
arr = []
for i in range(4):
    a = []
    for j in range(5):
        a.append('_')
    arr.append(a)
'''

arr = [
    ['_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_'],
     ['_', '_', '_', '_', '_']
]



def expl(y, x):
    direct = [(0, 1), (0, -1), (1, 1), (1, 0), (1, -1), (-1, 1), (-1, 0), (-1, -1)]
    for i, j in direct:
        dir_y = y + i
        dir_x = x + j
        if 0 <= dir_y < len(arr) and 0 <= dir_x < len(arr[0]):
            arr[dir_y][dir_x] = '#'

for i in range(2):
    y, x = map(int, input().split())
    expl(y, x)
for a in arr:
    print(*a)

