# evid =      [-1, 0, 0, 1, 2, 4, 4]
# timeStamp = [8 , 3, 5, 6, 8, 9, 10]
#
# 추적을 시작 할 index를 입력 받으세요
# 만약 5를 입력 받았다면,  **5번index**부터 추적을 시작합니다.
# 5번 index를 살펴보면 4번 index에서 출발했고, 9시에 도착했다는 것을 알 수 있습니다.
# 4번 index를 살펴보면 2번 index에서 출발했고, 8시에 도착했다는 것을 알 수 있습니다.
# 2번 index를 살펴보면 0번 index에서 출발했고, 5시에 도착했다는 것을 알 수 있습니다.
# 범죄가의 흔적들을 추적해가면 마지막에는 -1에 도달합니다.
# -1 이 있는 곳에서 범죄자를 잡을 수 있습니다.
# 범인은 0번 index부터 몇시에 몇번 index로 이동했는지 순서대로 출력하세요
# (재귀를 이용해서 범인을 추적)

'''
입력
추적을 시작할 index를 입력 받습니다 (0<=index<=6)

출력
A번 index(B) 형태로 추적상황 출력
A에는 추적한 위치에 해당하는 index번호
B에는 범인이 도착할시간을 'X시'의 형태로 출력. 단범인을 잡은 위치에서는 '출발'출력

입력예시
5

출력예시
0번 index(출발)
2번 index(5시)
4번 index(8시)
5번 index(9시) 
'''         #0   1  2  3  4  5  6
# evid =      [-1, 0, 0, 1, 2, 4, 4]
# st = ['6', '5', '4', '3', '2', '1']
#
# 0 0 0 0 1 0 0
# 0 0 0 0 1 0 0
# 0 0 1 0 0 0 0
# 0 1 0 0 0 0 0
# 1 0 0 0 0 0 0
# 1 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# timeStamp = [8 , 3, 5, 6, 8, 9, 10]
# V = len(evid)
# def dfs(n, st, V, adj_m):
#     stack = []  #stack 생성
#     visited = [0] * (V+1) #방문점 생성
#     visited[n] = 1 #시작점 방문 표시
#     # print(st[n], end = '')
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

######
evid = [-1, 0, 0, 1, 2, 4, 4]
timeStamp = [8, 3, 5, 6, 8, 9, 10]

N = int(input())
def DFS(idx):
    if evid[idx] == -1:
        print(f'{idx}번 index(출발)')
        return
    DFS(evid[idx])
    print(f'{idx}번 index({timeStamp[idx]}시)')
DFS(N)
