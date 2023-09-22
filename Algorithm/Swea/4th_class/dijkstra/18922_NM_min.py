import heapq

n, m = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(n)]
dist = [[float('inf')]*m for _ in range(n)]

xdir = [0, 0, 1, -1]
ydir = [-1, 1, 0, 0]

def dijkstra():
    pq = []
    dist[0][0] = MAP[0][0] #시작 지점의 최단거리는 해당 지점의 값
    heapq.heappush(pq, (MAP[0][0], 0, 0)) #시작지점 우선순위 큐에 넣기
    while pq:
        cost, y, x, = heapq.heappop(pq) #현재지점 y, x 그 지점까지의 거리 cost
        # 이미 확인한 좌표일 경우 (더 짧은 경로를 발견한 경우) continue
        if dist[y][x] < cost:
            continue
        for i in range(4):
            ny = y + ydir[i]
            nx = x + xdir[i]
            # 맵 범위를 벗어나는 경우 continue
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            nextcost = cost + MAP[ny][nx] #다음 지점까지의 거리
            # 이미 발견한 경로가 더 짧은 경우 continue
            if dist[ny][nx] <= nextcost:
                continue
            dist[ny][nx] = nextcost #최단거리 distance갱신
            heapq.heappush(pq, (nextcost, ny, nx)) #우선 순위 큐에 다음 지점 정보 넣기
    return  dist[n-1][m-1] #최단거리 반환
print(dijkstra())