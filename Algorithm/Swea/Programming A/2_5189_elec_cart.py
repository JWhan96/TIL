def cart(cur, start, total): # 현재구역, 시작구역, 총 배터리 사용량
    global result
    if cur == n -1: # 모든 구역을 다 돌았을 경우
        result = min(result, arr[start][0] + total) #총 배터리 사용량의 최소값 업데이트
        return
    for i in range(1, n): #모든 구역 탐색 -> 순열
        if visited[i] == 0 and start != i : # 아직 방문하지 않은 구역이고, 시작구역과 다른경우
            visited[i] = 1 #방문표시
            cart(cur +1, i, total + arr[start][i]) # 다음 구역이동
            visited[i] = 0 #방문표시 지우기
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0 for _ in range(n)]
    result = float('inf')
    cart(0,0,0)
    print(f'#{tc} {result}')