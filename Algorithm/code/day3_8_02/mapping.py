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