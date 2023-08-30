from collections import deque

def bfs(start, end):
    queue = deque([(start, 0)]) #큐에 시작노드와 초기거리 0넣기

    while queue:
        n, cnt = queue.popleft() # 현재노드와 거리 디큐

        if not visited[n]: #노드를 방문하지 않았다면
            visited[n] = 1

        for j in arr[n]:  # 현재 노드와 연결된 노드 탐색
            if not visited[j] and j == end: #목표노드도착
                return cnt +1 #거리 1반환
            elif not visited[j]: #아직 방문하지 않은 노드
                queue.append((j, cnt +1)) #인큐


    return 0 # 경로없으면 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[]for _ in range(V+1)] #인접행렬 초기화

    visited = [0] * (V+1)
    for i in range(E): #간선 개수만큼 반복
        n1, n2 = map(int, input().split())
        arr[n1].append(n2)
        arr[n2].append(n1)
    start, end = map(int, input().split())

    print(f'#{tc} {bfs(start, end)}')