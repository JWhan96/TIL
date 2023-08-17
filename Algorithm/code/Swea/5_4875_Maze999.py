####강사님 코드
def maze():
    while stack:
        y, x = stack.pop()  # 현재 위치를 스택에서 꺼냄
        arr[y][x] = -1  # 지나간길 표시
        for i in range(4):  # 4방향 탐색
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if arr[ny][nx] == 3:  # 도착점을 찾았다 -> 1 반환
                    return 1
                elif arr[ny][nx] == 0:    # 갈 수 있는 곳을 모두 stack에 추가
                    stack.append((ny, nx))  # 튜플
    return 0  # 도착점을 못찾으면 -> 0반환
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]  # 미로 정보
    dy = [0, 1, 0, -1]  # 세로
    dx = [1, 0, -1, 0]  # 가로
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 2:  # 시작점 찾기
                stack = [(y, x)]  # 시작점 스택에 추가
                break
    print(f'#{tc} {maze()}')