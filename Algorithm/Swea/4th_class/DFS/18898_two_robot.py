#동굴의 방 개수, 두로봇이 위치한 방 번호
N, s, e = map(int, input().split())
al = [[] for _ in range(N + 1)] #al 리스트는 각 방과 연결된 방의 정보
visited = [0 for _ in range(N + 1)] # visited리스트 : 해당 방을 방문했는지 여부
sum_v = 0
MIN = float('inf')
MAX = float('-inf')
#주어진 시작위치(node) 부터 목표위치(dest)까지 이동하는 모든 경로 탐색
def dfs(node, dest):
    global sum_v, MIN, MAX
    #만약 목표위치에 도달하면, 최솟값(이동한 거리 - 가장 긴 통로의 길이) 확인
    if node == dest:
        if sum_v - MAX < MIN:
            MIN = sum_v - MAX
        return
    for next in al[node]:
        if visited[next[0]] == 1: #이미 방문한 방은 다시 방문 x
            continue
        sum_v += next[1]
        visited[next[0]] = 1
        temp = MAX
        #지금까지 방문한 통로중 가장 긴것을 MAX에 저장
        if next[1] > MAX:
            MAX = next[1]
        dfs(next[0], dest)
        #dfs호출 후 이전 상태로 복원
        visited[next[0]] = 0
        sum_v -= next[1]
        MAX = temp
for _ in range(N - 1):
    from_v, to_v, cost = map(int, input().split())
    al[from_v].append((to_v, cost))
    al[to_v].append((from_v, cost))
visited[s] = 1 #dfs탐색 전에 로봇이 위치한 방 방문 처리
dfs(s, e)
#만약 두 로봇이 이미 통신이 가능한 위치에 있으면 0을 출력
print(MIN if MIN != float('inf') else 0)