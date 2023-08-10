# 8개의 알파벳으로 구성 된 문자열과 대응되는 인접행렬을 입력받기
# 아래 이미지는 입력 예시에 해당하는 트리입니다.
# 0번 알파벳부터 DFS로 노드들을 탐색하면서 출력

# 첫번째에 8개의 알파벳으로 이루어진 문자열
# 이어지는 8개의 줄에 걸쳐 인접행렬에 대한 정보
# 각 인접행렬의 줄 번호 i, 칸번호j, 해당위치의 값 Aij라고 할때
# Aij가 1이면 i번 알파벳에서 j번 알파벳으로 갈 수 있다는 것을 의미

'''
RKFCBICM
0 1 1 1 0 0 0 0
0 0 0 0 1 1 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

출력예시
RKBIFCCM
'''
# st = list(input())
# arr = [list(map(int, input().split())) for _ in range(8)]
# V = 8
# for i in range(8):
#     for j in range(8):
#         if arr[i][j] == 1:
#             arr[j][i] = 1
# def dfs(n, st, V, adj_m):
#     stack = []  #stack 생성
#     visited = [0] * (V+1) #방문점 생성
#     visited[n] = 1 #시작점 방문 표시
#     print(st[n], end = '')
#     while True:
#         for w in range(1, V): # 현재 정점 n에 인접하고 미방문 w 찾기
#             if adj_m[n][w] == 1 and visited[w] ==0:
#                 stack.append(n)
#                 n = w  #새로 옮겨갈 위치 w
#                 print(st[n], end = '')
#                 visited[n] = 1 # w 방문 표시
#                 break # for w,n에 인접인 c찾은경우
#         else:
#             if stack: #스택에 지나온 정점이 남아있으면
#                 n = stack.pop() #pop해서 다른 w찾을 준비
#             else: #스택이 비어있으면
#                 break #탐색끝
#     return
# dfs(0, st, V, arr)

lst = list(input()) #노드 입력
N = len(lst) # 노드갯수
adj = [list(map(int, input().split())) for _ in range(N)] # 인접행렬 입력
visited = [False for _ in range(N)] # 방문여부를 저장하는 리스트 처음에는 False 초기화

def DFS(v):
    print(lst[v], end = '') #현재 방문한 노드 출력
    visited[v] = True

    for i in range(N):
        if adj[v][i] and not visited[i]: #연결되어 있고, 아직 방문하지 않았다면
            DFS(i)  # 탐색 계속

DFS(0)