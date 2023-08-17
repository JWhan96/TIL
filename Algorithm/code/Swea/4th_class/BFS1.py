arr = [
    [0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1],
    [0, 0, 1, 1, 0, 0]
       ]
N = int(input())

def BFS(N, n, arr):
    visited = [0] * n
    queue = []
    queue.append(N)
    visited[N] = 1
    while queue:
        t = queue.pop(0)
        print(t)
        for i in range(6):
            if arr[t][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1
BFS(N, 6, arr)