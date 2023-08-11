# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
arr = list(map(int, input().split()))
max_v = arr[0]
min_v = arr[0]
for i in range(len(arr)):
    if max_v < arr[i]:
        max_v = arr[i]
print(max_v)
for i in range(len(arr)):
    if min_v > arr[i]:
        min_v = arr[i]
print(min_v)
##############
# max_idx = arr.index(max_v)
# min_idx = arr.index(min_v)
min_idx = 0
max_idx = 0
for i in range(1, 21):
    ##가장 오른쪽
    if arr[min_idx] >= arr[i]:
        min_idx = i
    ## 가장 왼쪽
    if arr[max_idx] < arr[i]:
        max_idx = i

print(max_idx)
print(min_idx)