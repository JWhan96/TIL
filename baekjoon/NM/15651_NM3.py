N, M = map(int, input().split())
lst = []
def NM():
    if len(lst) == M:
        print(*lst)
        return

    for i in range(1, N+1):
        lst.append(i)
        NM()
        lst.pop()

NM()