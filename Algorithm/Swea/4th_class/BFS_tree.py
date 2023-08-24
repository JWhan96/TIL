arr = [
    [0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
       ]
N = int(input())

def BFS(N, n, arr):
    visited = [0] * n
    queue = []
    queue.append(N)
    visited[N] = 1
    while queue:
        print(queue[0], end = ' ')
        t = queue.pop(0)

        for i in range(6):
            if i == t:
                for j in range(6):
                    if arr[i][j] == 1:
                        if visited[j] == 0:
                            queue.append(j)
                            visited[j] = 1
BFS(N, 6, arr)

# from collections import deque
#
# k = int(input())
# def bfs(now):
#     q = deque()
#     q.append(now) #시작노드를 큐에 추가
#     while q:
#         now = q.popleft() #큐에서 하나의 노드 꺼낸후 출력
#         print(now, end = ' ')
#         for i in range(6): #현재노드와 연결된 모든 노드 확인
#             if arr[now][i] == 1: #현재 노드와 i번째 노드가 연결되어 있다면
#                 q.append(i) #i번째 노드를 큐에 추가
# bfs(k)