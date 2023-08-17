from collections import deque
T = int(input())
for tc in range(1, T+1):
    N = int(input())

    maze = [list(map(int, input())) for _ in range(N)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]


    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        count = 0
        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue

                if maze[nx][ny] == 1:
                    continue
                # if maze[nx][ny] == 2:
                #     bfs(nx, ny)
                if maze[nx][ny] == 0:
                    maze[nx][ny] = maze[x][y] + 1
                    count += 1
                    queue.append((nx, ny))
                if maze[nx][ny] == 3:
                    return count
        return 0



    print(bfs(4, 3))
