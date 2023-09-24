# def cart(cur, start, total): # 현재구역, 시작구역, 총 배터리 사용량
#     global result
#     if cur == n -1: # 모든 구역을 다 돌았을 경우
#         result = min(result, arr[start][0] + total) #총 배터리 사용량의 최소값 업데이트
#         return
#     for i in range(1, n): #모든 구역 탐색 -> 순열
#         if visited[i] == 0 and start != i : # 아직 방문하지 않은 구역이고, 시작구역과 다른경우
#             visited[i] = 1 #방문표시
#             cart(cur +1, i, total + arr[start][i]) # 다음 구역이동
#             visited[i] = 0 #방문표시 지우기
# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     visited = [0 for _ in range(n)]
#     result = float('inf')
#     cart(0,0,0)
#     print(f'#{tc} {result}')


def f(i, N):
    global result
    if i == N: # 순열 완성
        p.append(1)
        min_v = 0
        for j in range(N):
            #1231
            min_v += arr[p[j]-1][p[j+1]-1]
        if min_v < result:
            result = min_v
        p.pop()
        return
    else:
        for j in range(N):
            if used[j] == 0:
                # 첫 번째 요소가 1이 아닌 경우에는 더 이상 진행하지 않음
                if i == 0 and lst[j] != 1:
                    continue

                p[i] = lst[j]
                used[j] = 1
                f(i+1, N)
                used[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    lst = [i for i in range(1,N+1)]
    used = [0] * N
    p = [0] * N
    result = float('inf')
    f(0, N)
    print(f'#{tc} {result}')