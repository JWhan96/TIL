N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
lst = []
def NM():

    if len(lst) == M:
        print(*lst)
        return

    for i in range(N):
        if arr[i] not in lst:
            lst.append(arr[i])
            NM()
            lst.pop()

NM()