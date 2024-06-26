'''
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5

'''

# 내가 갈 수 있는 경로 중 누적거리가 제일 짧은 것부터 고르자
import heapq

# 입력
n, m = map(int, input().split())
# 인접 리스트
graph = [[] for i in range(n)]
for _ in range(m):
    f, t, w = map(int, input().split())
    # 단방향이라 하나만
    graph[f].append([t, w])

# 1. 누적 거리를 계속 저장
INF = float('inf') 
distance = [INF] * n

def dijkstra(start):
    # 2. 우선 순위 큐
    pq = []
    # 출발점 초기화
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        # 현재시점에서
        # 누적 거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(pq)

        # 이미 방문한 지점 + 누적거리가 더 짧게 방문한 적이 있다면
        if distance[now] < dist:
            continue
        
        #인접 노드를 확인
        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            # next_node로 가기 위한 누적 거리
            new_cost = dist + cost
            
            # 누적 거리가 기존보다 크다면?
            if distance[next_node] <= new_cost:
                continue

            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))

dijkstra(0)
print(distance)

