N = int(input())
arr = list(map(int, input().split()))
lst = []
cnt = 0
for i in range(2, 1001):
    lst.append(i)
# .remove 주의사항 : index 처리
j = 0
k = 1
while True:
    L = len(lst)
    if j == L :
        break
    if j + k == L:
        k = 1
        j += 1
    if j+k < L:
        if lst[j+k] % lst[j] != 0:
            k += 1
        else:
            lst.remove(lst[j+k])


# 소수인지 판별
for i in range(N):
    if arr[i] not in lst:
        continue
    else:
        cnt += 1

print(cnt)