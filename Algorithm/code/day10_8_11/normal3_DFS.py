N = int(input())
M = int(input())
arr = [[0] * N for _ in range(N)]
visited = [0] * N
for _ in range(M):
    c1, c2 = map(int, input().split())
    arr[c1-1][c2-1] = arr [c2-1][c1-1] = 1
def DFS(v):
    visited[v] = 1
    for i in range(N):
        if arr[v][i] == 1 and not visited[i]:
            DFS(i)
DFS(0)
print(sum(visited)-1)