import heapq


node, edge = map(int, input().split()) # 노드 n, 간선 e
graph = [[] for _ in range(node)]
distance = [float('inf')] * node #최단 거리 테이블을 모두 초기화
visited = [False] * node
pq = [] # 우선순위 큐

for _ in range(edge):
    from_node, to , cost = map(int, input().split())
    graph[from_node].append((to, cost)) #from_node에서 to로 가는 비용이 cost

def dijkstra():
    distance[0] = 0 #시작 노드 최단거리 0으로 초기화
    heapq.heappush(pq, (0,0)) #(비용, 노드)
    while pq:
        cur_cost, cur_node = heapq.heappop(pq) #우선 순위 큐에서 현재 노드와 현재 비용을 가져옴
        if visited[cur_node]: #이미방문한 노드라면 continue
            continue
        visited[cur_node] = True #현재 방문한 노드 처리
        #현재 노드와 연결된 다른 노드를 확인
        for next_node, edge_cost in graph[cur_node]:
            total_cost = cur_cost + edge_cost #총비용 계산
            if distance[next_node] > total_cost: #최단 거리 테이블 갱신 조건 확인
                distance[next_node] = total_cost
                heapq.heappush(pq, (distance[next_node], next_node)) #우선 순위 큐에 새로운 노드 정보 추가

dijkstra()
if distance[node - 1] == float('inf'):
    print('impossible')
else: #도착 지점에 도달하는 비용 출력
    print(distance[node - 1])
