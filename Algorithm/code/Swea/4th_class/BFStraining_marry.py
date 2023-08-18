from pprint import pprint
def BFS(coco, N):
    visited = [0] * (N+1)  # 방문여부 행렬
    queue = []
    queue.append(coco)    # 시작노드 큐에 추가
    visited[coco] = 1     # 시작노드 방문 표시
    lst = []
    while queue:  # 큐추가/팝 반복하며 모든 요소 탐색할 때까지(큐가 빌 때까지)
        t = queue.pop(0)  # 첫 인덱스 요소 pop(큐 특성/선입선출)
        # print(t)
        for i in range(N+1):
            if arr[t][i] == 1 and visited[i] == 0:  # 간선이 있고 방문한적이 없는 노드라면
                lst.append(i)
                queue.append(i)  # 큐에 추가
                visited[i] = 1
    return lst

N = int(input())
T = int(input())
arr = [[0] * (N+1) for _ in range(N+1)]

for i in range(T):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1
coco = int(input())
some = int(input())

result = BFS(coco, N)

if some in result:
    print('YES')
else:
    print('NO')

######
# from collections import deque
# def bfs(start, target):
#     q = deque
#     q.append(start)
#     visited[start] = 1
#     while q:
#         now = q.popleft()
#         for i in range(1, N+1):
#             if arr[now][i] == 0:
#                 continue
#             if visited[i] ==1:
#                 continue
#             if i == target:
#                 print('Yes')
#                 return
#             q.append(i)
#             visited[i] = 1
#     print('No')
#
# N = int(input())
# T = int(input())
# arr = [[0] * (N+1) for _ in range(N+1)]
# visited = [0] *(N+1)
# for i in range(T):
#     a, b = map(int, input().split())
#     arr[a][b] = 1
#     arr[b][a] = 1
# coco = int(input())
# some = int(input())
#
# bfs(coco, some)