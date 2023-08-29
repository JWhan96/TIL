N, M = map(int, input().split())
lst = []
cnt = 1
def NM():
    global cnt
    if len(lst) == M:
        print(*lst)
        return

    for i in range(cnt, N+1):

        lst.append(i)
        cnt = i
        NM()
        lst.pop()

NM()