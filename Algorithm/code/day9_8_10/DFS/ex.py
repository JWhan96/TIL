st = list(input())
N = len(st)
arr = [list(map(int, input().split())) for _ in range(N)]

def DFS(n):
    stack = []
    visited = [0] * N
    visited[n] = 1
    print(st[n], end= '')
    while True:
        for w in range(N):
            if arr[n][w] ==1 and visited[w] == 0:
                stack.append(n)
                n = w
                print(st[n], end= '')
                visited[n] = 1
                break
        else:
            if stack:
                n = stack.pop()
            else:
                break
    return

DFS(0)
