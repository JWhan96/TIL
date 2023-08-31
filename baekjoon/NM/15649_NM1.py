N, M = map(int, input().split())
lst = []
for i in range(N):
    lst.append(i+1)
lst1 = []

def NM():
    global lst1
    if len(lst1) == M:
        print(*lst1)
        return

    for i in lst:

        if i not in lst1:

            lst1.append(i)
            NM()
            lst1.pop()

NM()
