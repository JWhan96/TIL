'''
33531
22426
49234
11111
33592    대각선 왼쪽위 오른쪽위
         왼쪽아래 오른쪽아래
map배열을 하드코딩
그리고 map에서 대각선방향(왼쪽위아래 오른쪽 위아래)의 합이 가장 큰 값이 나오는 좌표 (y,x)출력
단 대각성 방향의 합을 구하는 sum(y,x)함수를 만들어서 사용
sum(y,x) 는 특정 좌표 (y,x)에서 대각선 방향의 합을 반환하는 함수

int sum(int y, int x){
    (y,x)죄표로 부터 대각선 방향의 합 반환

}
*direct 기법사용하기
'''

arr = [
    [3, 3, 5, 3, 1],
    [2, 2, 4, 2, 6],
    [4, 9, 2, 3, 4],
    [1, 1, 1, 1, 1],
    [3, 3, 5, 9, 2]
]



max_result = 0
max_y = 0
max_x = 0

def sum(y, x):
    # 대각선의 방향
    direct = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    result = 0
    for i, j in direct:
        dir_y = y + i
        dir_x = x + j
        if 0 <= dir_y < len(arr) and 0 <= dir_x < len(arr[0]):
            result += arr[dir_y][dir_x]
    return result

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if sum(i, j) > max_result:
            max_result = sum(i, j)
            max_y, max_x = i, j
print(f'{max_y, max_x} {max_result}')












# def sum(y, x):
#     # 대각선 합?
#
#
#
#
#

#
#
# #(3,2)