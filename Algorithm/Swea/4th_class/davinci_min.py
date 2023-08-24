from itertools import permutations

N, M = map(int, input().split())
arr = list(map(int, input().split()))
lst1 = []
lst2 = []
for i in arr:
    if i >= 0:
        lst1.append(i)
    else:
        lst2.append(i)
new_arr = list(map(abs, arr))
new_sorted = sorted(new_arr, reverse = True)
lst1_sorted = sorted(lst1, reverse = True)
lst2_sorted = sorted(lst2)
print(new_sorted, lst1_sorted, lst2_sorted)
sorted_arr = []
if lst2_sorted:
    for i in new_sorted:

        for j in lst2_sorted:
            if -i in lst2_sorted and j not in sorted_arr:
                sorted_arr.append(j)
            elif i in lst1_sorted and i not in sorted_arr:
                sorted_arr.append(i)
else:
    sorted_arr = new_sorted[:]
print(sorted_arr)
check = list(permutations(sorted_arr, M))
print(check)
flag = 0
def Check():

    global flag
    if lst2_sorted:
        for i in check:
            gop = 1
            for j in i:
                gop *= j
                if gop < 0:
                    print(gop)
                    flag = 1
                    break

            if flag == 1:
                break
    else:
        i = []
        for k in range(N-1, N-M-1, -1):
            i.append(sorted_arr[k])
        else:
            return i

    return i
result1 = Check()
print(*sorted(result1))
##########################

# def Dfs():
#     stack = []
#     visited = [0] * N
#     if lst2_sorted:
#
#         for i in range(N):
#
#             if 조건 and visited[i] ==0:
#
#             if len(stack) == 3 and 곱 < 0 :


#
#
# import copy
# N, M = map(int, input().split())
# lst = list(map(int, input().split()))
# path = [] #선택된 패들의 값을 저장할 리스트
# used = [0] * N # 패가 사용되었는지 체크
# Min = 21e8
# result = []
#
# def DFS(level, Sum):
#     global Min, path, result
#     if level == M: #패를 모두 선택했다면
#         if Sum < Min:
#             Min = Sum
#             result = copy.deepcopy(path)
#         return
#
#     for i in range(N):
#         if used[i] == 1: #이미 사용된 패라면 건너뜀
#             continue
#         path.append(lst[i]) #패를 선택하고 path에 추가
#         used[i] = 1
#         DFS(level + 1, Sum * lst[i])
#         used[i] = 0 #복구 (백트래킹)
#         path.pop()
# DFS(0, 1) #초기레벨 0 , 초기곱 1
# result.sort()
# print(*result)