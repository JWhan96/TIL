N, M = map(int, input().split())
lst = []
for i in range(N):
    lst.append(i+1)
lst1 = []
cnt = 1
def NM():
    global lst1
    global cnt
    if len(lst1) == M:
        print(*lst1)
        return

    for i in range(cnt, N+1):

        if i not in lst1:

            lst1.append(i)
            cnt = i
            NM()
            lst1.pop()

NM()
