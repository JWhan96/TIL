N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
lst = []
cnt = 0
def NM():
    global cnt
    if len(lst) == M:
        print(*lst)
        return

    for i in range(cnt ,N):

        lst.append(arr[i])
        cnt = i
        NM()
        lst.pop()

NM()