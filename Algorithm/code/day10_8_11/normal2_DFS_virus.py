'''
입력
7
6
1 2
2 3
1 5
5 2
5 6
4 7

출력
4
'''
# N = int(input())
# M = int(input())
# arr = [[0] * N for _ in range(N)]
# visited = [0] * N
# for _ in range(M):
#     c1, c2 = map(int, input().split())
#     arr[c1-1][c2-1] = arr [c2-1][c1-1] = 1
# def DFS(v):
#     visited[v] = 1
#     for i in range(N):
#         if arr[v][i] == 1 and not visited[i]:
#             DFS(i)
# DFS(0)
# print(sum(visited)-1)

#########방법 2
N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]
visited = [0] * N
cnt = 0
for _ in range(M):
    c1, c2 = map(int, input().split())
    arr[c1].append(c2) #c1노드와 연결된 c2노드를 arr에 추가
    arr[c2].append(c1) #c2노드와 연결된 c1노드를 arr에 추가
visited[1] = 1
def DFS(c1):
    global cnt
    for i in arr[c1]:
        if not visited[i]:
            visited[i] = 1
            cnt += 1
            DFS(i)

DFS(1)
print(cnt)