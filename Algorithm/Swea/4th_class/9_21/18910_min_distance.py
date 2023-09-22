#swea 최소 이동 거리 - 다익스트라
def dijkstra(start):
    dist[start] = 0 #시작 노드 최단 거리 distance 0으로 설정
    for _ in range(N + 1):
        min_idx = -1 #최소거리 노드의 인덱스
        min_value = float('inf')

        #아직 방문하지 않은 노드 중에서 최소거리 노드 찾기
        for i in range(N + 1):
            if not visited[i] and dist[i] < min_value:
                min_idx = i
                min_value = dist[i]
        visited[min_idx] = 1 #최소 거리 노드 방문 처리

        # 최소거리 노드와 연결된 다른 노드들이 거리 갱신
        for i in range(N + 1):
            if arr[min_idx][i] and not visited[i]:
                dist[i] = min(dist[i], dist[min_idx] + arr[min_idx][i])
T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    arr = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    visited = [0 for _ in range(N + 1)]
    dist = [float('inf') for _ in range(N + 1)]
    #시작노드s, 도착노드 e, 가중치 w
    for s, e, w in edges:
        arr[s][e] = w
    dijkstra(0)
    print(f'#{tc} {dist[N]}')