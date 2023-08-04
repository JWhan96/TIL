N = int(input())
arr = [list(map(int, input().split())) for _ in range(5)]
K = int(input())


direct = [(1,1), (1, -1), (-1, 1), (-1, -1)]

def magic(y, x):
    dy = [-1, 1, -1, 1]
    dx = [1, 1, -1, -1]
    result = 0
    for i in range(4):
        for j in range:
            ny = y + dy[i]*j
            nx = x + dx[i]*j
            if 0 <= ny <N and 0 <= nx < N:
                result += arr[ny][nx]
    return result
result_list = []

for i in range(N):
    for j in range(N):
        result_list.append(magic(i, j))
print(max(result_list))

