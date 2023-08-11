# 트리 DFS를 돌리려 한다
# 숫자 n과 인접행렬을 입력 받는다
# DFS를 돌리고, 탐색 순서대로 출력
#
# [유의사항]
# 1. 노드 값은 없으며 노드번호를 출력하면 된다.
# 2. 항상 0번부터 탐색을 시도
# 3. 자식 노드가 여러개라면, 노드번호가 작은 것부터 탐색
# 4. 1 <= n <= 100
# 5. 노드의 번호는 0 ~ n-1번까지 존재
''''
입력
첫번 째 줄에 노드의 수 n을 입력받음
다음 n개의 줄에 걸쳐 인접행렬 정보
각 인접행렬의 줄번호i, 칸번호 j, 해당위치의 값 Aij라고 할 때
Aij가 1이면 i번 노드에서 j번 노드로 갈수 있다는 것을 의미
출력
0번에서 시작 DFS로 탐색하였을때 방문한 노드번호들을 순서대로 공백으로 구분하여 출력

입력 예시
5
0 1 1 0 0
0 0 0 1 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
출력예시
0 1 3 4 2
'''
n = int(input())
st = []
for i in range(n):
    st.append(i)
arr = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            arr[j][i] = 1
def DFS(n, st, V, adj_m):
    stack = []  #stack 생성
    visited = [0] * (V+1) #방문점 생성
    visited[n] = 1 #시작점 방문 표시
    print(st[n], end = ' ')
    while True:
        for w in range(1, V): # 현재 정점 n에 인접하고 미방문 w 찾기
            if adj_m[n][w] == 1 and visited[w] == 0:
                stack.append(n)
                n = w  #새로 옮겨갈 위치 w
                print(st[n], end = ' ')
                visited[n] = 1 # w 방문 표시
                break # for w,n에 인접인 c찾은경우
        else:
            if stack: #스택에 지나온 정점이 남아있으면
                n = stack.pop() #pop해서 다른 w찾을 준비
            else: #스택이 비어있으면
                break #탐색끝
    return
DFS(0, st, n, arr)


########강사님 코드
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# def DFS(now):
#     #현재 방문한 노드 출력
#     print(now, end = ' ')
#     for i in range(N):
#         #현재 노드와(now) i번째 노드가 연결되어 있다면
#         if arr[now][i] == 1:
#             #재귀적으로 i번째 노드 방문
#             DFS(i)

# 첫번째 노드부터 탐색 시작
# DFS(0)

