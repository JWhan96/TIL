def BFS(N):

    visited = [0] * (N+1)  # 방문여부 행렬
    queue = []
    queue.append(start)    # 시작노드 큐에 추가
    visited[start] = 1     # 시작노드 방문 표시
    lst = []
    lst.append(start)
    count = 0
    while queue:  # 큐추가/팝 반복하며 모든 요소 탐색할 때까지(큐가 빌 때까지)
        t = queue.pop(0)  # 첫 인덱스 요소 pop(큐 특성/선입선출)
        # 만약 카운트가 넘으면 append를 안하므로 pop만 반복 하다가 que가 비면 while탈출
        print(count,t)
        if count <= limit: ##count가 환승 횟수이하 일 때만
            for i in range(N+1):
                if arr[t][i] == 1 and visited[i] == 0:  # 간선이 있고 방문한적이 없는 노드라면
                    lst.append(i) # 가능 지역 lst에 추가
                    queue.append(i)  # 큐에 추가
                    visited[i] = 1

            else: # for문이 끝나면 다음 BFS진행표시를 위해 count += 1
                count += 1


    return lst

N , T = map(int, input().split())
arr = [[0] * (N+1) for _ in range(N+1)]

for i in range(T):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1
start, limit = map(int, input().split())


result = BFS(N)
print(len(result), result)

#######
# from collections import deque
# N, M = map(int, input().split())
# arr = [[0] * (N + 1) for _ in range(N + 1)]
# visited = [0] * (N + 1)
# for _ in range(M):
#     A, B = map(int, input().split())
#     arr[A][B] = 1
#     arr[B][A] = 1 #양뱡향 그래프
# R, K = map(int, input().split())
# cnt = 0
#
# def bfs(node):
#     global cnt
#     q = deque()
#     q.append(node)
#     visited[node] = 1
#     while q:
#         now = q.popleft()
#         if visited[now] - 1 <= K: #탐색 깊이가 K 이하면 카운트 증가
#             cnt += 1
#         if visited[now] - 1 > K:
#             break
#         for i in range(1, N+1):
#             if arr[now][i] == 0: #연결되지 않은 노드는 건너띔
#                 continue
#             if visited[i] > 0: #이미 방문한 노드 건너뜨ㅟㅁ
#                 continue
#             visited[i] = visited[now] + 1
#             q.append(i)
# bfs(R)
# print(cnt)