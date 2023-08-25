
def solve():
    ans = 0 #최대 서비스 제공 집의 수
    K = N + 1 #가능한 최대의 서비스 영역 크기
    for k in range(K, 0, -1):
        cost = k * k + (k - 1) * (k - 1)
        for y in range(N):
            for x in range(N):
                cnt = 0 #현재 위치에서 서비스 가능한 집의 수
                for hy, hx in houses:
                    dist = abs(hy - y) + abs(hx - x)
                    if dist < k : #거리가 k보다 작으면 서비스 가능 -> count 증가
                        cnt += 1
                if cnt * M - cost >= 0: #수익이 운영비용보다 크거나 같은경우
                    ans = max(ans, cnt)
        if ans != 0:
            return ans
    return ans

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    houses = [] #집의 위치
    for i in range(N):
        for j in range(N):
            if arr[i][j]: #집이 있는 위치를 찾으면 리스트에 추가
                houses.append((i, j))
    result = solve()
    print(f'#{tc} {result}')
