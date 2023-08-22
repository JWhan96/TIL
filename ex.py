N = int(input())
arr = []
for i in range(1, N+1):
    arr.append(str(i))
# print(arr)

for i in range(len(arr)):
    clab = 0
    if '3' in arr[i] or '6' in arr[i] or '9' in arr[i]:
        clab += arr[i].count('3')
        clab += arr[i].count('6')
        clab += arr[i].count('9')
        arr [i] = clab*'-'
    else:
        arr[i] = arr[i]
print(*arr)