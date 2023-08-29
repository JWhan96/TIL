N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
lst = []
cnt = 0
result = []
arr_cnt = []
for i in range(N):
    arr_cnt.append(arr.count(arr[i]))
def NM():
    global cnt

    if len(lst) == M:
        if lst not in result:
            result.append(lst[:])


            print(*lst)
        return

    for i in range(N):

        if arr[i] not in lst or arr_cnt[i] > 1:
            lst.append(arr[i])

            NM()

            lst.pop()
NM()
