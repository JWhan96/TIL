# arr = [[1, 0, 2, 0, 1, 0, 1],
#        [0, 2, 0, 0, 0, 0, 0],
#        [0, 0, 1, 0, 0, 1, 0],
#        [0, 0, 0, 0, 1, 2, 2],
#        [0, 0, 0, 0, 0, 1, 0],
#        [0, 0, 2, 1, 0, 2, 1],
#        [0, 0, 1, 2, 2, 0, 2]
# ]
#
#
# T = 10
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split()))for _ in range(N)]
#     arr_t = [list(item) for item in zip(*arr)]
#
#     cnt = 0
#
#     for i in range(N):
#         while True:
#
#             if arr_t[i] and (arr_t[i][0] == 2 or arr_t[i][0] == 0):
#                 arr_t[i].pop(0)
#             if arr_t[i] and (arr_t[i][-1] == 1 or arr_t[i][-1] == 0):
#                 arr_t[i].pop(-1)
#             if not arr_t[i]:
#                 break
#             if arr_t[i][0] == 1 and arr_t[i][-1] == 2:
#
#                 break
#
#         stack = []
#
#         if arr_t[i]:
#             for j in range(len(arr_t[i])):
#                 if not stack and arr_t[i][j] == 1:
#                     stack.append(1)
#                 if stack and arr_t[i][j] == 2:
#                     stack.pop()
#                     cnt += 1
#
#     print(f'#{tc} {cnt}')
#

###
T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]
    cnt = 0 # 교착상태
    for j in range(N):
        y, x = 0, j
        stack = []
        while y< N:
            if not stack and arr[y][x] == 1:
                stack.append(1)
            elif stack and arr[y][x] ==2 :
                stack.pop()
                cnt += 1
            y += 1
    print(cnt)
import time

def measure_execution_time(code_block):
    start_time = time.time()
    code_block()
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

# 주어진 코드 블록을 실행하여 시간 측정


code_block = lambda: arr = [list(map(int, input().split()))for _ in range(N)]
execution_time = measure_execution_time(code_block)
print("Execution time:", execution_time, "seconds")