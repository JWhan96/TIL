# N x N 인접행렬 트리를 입력받기
# 0번 node에서부터 DFS로 탐색하여 LEVEL2에 도착할 때마다 경로를 출력
#
#           0
#
#    1             2
#
# 3  4  5       6  7  8
#
# 위와 같은 트리를 입력받았따면
# 0 1 3
# 0 1 4
# 0 1 5
# 0 2 6
# 0 2 7
# 0 2 8
'''
입력
첫 번째에 노드의 개수 n
이어지는 n개의 줄에 인접행렬에 대한 정보

각 인접행렬의 줄 번호i, 칸번호j, 해당위치의 값 Aij라 할때
Aij가 1이면 i번 알파벳에서 j번 알파벳으로 갈 수 있다는 것을 의미

출력
Level2에 도착할 때 마다 탐색 경로 출력

입력예시
9
0 1 1 0 0 0 0 0 0
0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 1 1 1
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0

출력예시
0 1 3
0 1 4
0 1 5
0 2 6
0 2 7
0 2 8
'''

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def DFS(n, V, adj_m):

    stack = []  #stack 생성
    visited = [0] * (V+1) #방문점 생성
    visited[n] = 1 #시작점 방문 표시

    while True:

        for w in range(1, V): # 현재 정점 n에 인접하고 미방문 w 찾기
            if adj_m[n][w] == 1 and visited[w] == 0:
                stack.append(n)

                n = w  #새로 옮겨갈 위치 w
                stack.append(n)
                if len(stack) == 3:
                    for i in stack:
                        print(i, end = ' ')
                    print()
                stack.pop()

                visited[n] = 1 # w 방문 표시
                break # for w,n에 인접인 c찾은경우
        else:
            if stack: #스택에 지나온 정점이 남아있으면
                n = stack.pop() #pop해서 다른 w찾을 준비
            else: #스택이 비어있으면
                break #탐색끝
    return

DFS(0, n, arr)

#############강사님코드
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# visited = [0] * 3
#
# def DFS(now, level):
#     global visited
#     visited[level] = str(now)
#     if level == 2:
#         print(' '.join(visited))
#     for i in range(N):
#         if arr[now][i] == 1:
#             DFS(i, level +1)
# DFS(0, 0)