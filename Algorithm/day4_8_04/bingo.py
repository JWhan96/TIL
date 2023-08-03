#방향 배열
from pprint import pprint

# arr = [list(map(int, input().split())) for _ in range(5)]
# solut = []
# for _ in range(5):
#     solut.extend(list(map(int, input().split())))
# print(arr)
# print(solut)
#
#
# direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#
# for i in solut:
#     for j in range(5):
#         for k in range(5):
#             if arr[j][k] == i:
#                 arr[j][k] = -1
#
#
# if True:#5개 되면
#     print(i)
# if True:#대각선
#     print(i)
# if True:#반대 대각선
#     print(i)

###########강사님
board = [int(num) for _ in range(5) for num in input().split()]
# board = [list(map(int, input().split())) for _ in range(5)]
call = [int(num) for _ in range(5) for num in input().split()]
cnt = 0
print(board, call)
x_list = [0] * 10
y_list = [0] * 10
di_list1 = [0] * 10
di_list2 = [0] * 10

for n in call:
    #부른 숫자의 인덱스 찾기
    a = board.index(n)
    # 인덱스 이용해 해당 숫자의 위치 x, y계산
    x, y = a//5, a % 5
    #가로 세로 대각선 빙고 개수 카운트증가
    x_list[x] += 1
    y_list[y] += 1
    #x와 y의합?
    # 00 , 11, 22, 33, 44
    di_list1[x+y] += 1
    # y-x =4?
    #04, 13, 22, 31, 40
    di_list2[y-x+4] += 1
    if x_list[x] == 5:
        cnt += 1
    if y_list[y] == 5:
        cnt += 1
    if di_list1[x + y] == 5 or di_list2[y - x + 4] == 5:
        cnt += 1
    if cnt == 3:
        print(n)
        break