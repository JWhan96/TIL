from pprint import pprint
N, M = map(int, input().split())
arr = [[0] * N for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    arr[u-1][v-1] = 1
pprint(arr)
cnt = 0
lst = [1, 2, 3, 4, 5, 6]

def DFS(n, N, arr):

    stack = []  #stack 생성
    visited = [0] * (N+1) #방문점 생성
    visited[n] = 1 #시작점 방문 표시

    while True:
        global cnt
        for w in range(0, N): # 현재 정점 n에 인접하고 미방문 w 찾기


            if arr[n][w] == 1 and visited[w] == 0:
                stack.append(n)

                n = w  #새로 옮겨갈 위치 w
                # print(f'n = {n}')
                stack.append(n)
                # if len(stack) >= 3:
                #     for i in stack:
                #         print(i+1, end = ' ')
                #     print()
                # print(f'stack = {stack[0]}')
                stack.pop()

                # print(k)


                visited[n] = 1 # w 방문 표시

                break # for w,n에 인접인 c찾은경우


        else:

            # if k == stack[0]:
            #     cnt += 1

            if stack: #스택에 지나온 정점이 남아있으면
                n = stack.pop() #pop해서 다른 w찾을 준비
            else: #스택이 비어있으면
                break #탐색끝
    return

for i in range()
DFS(0, N, arr)
print('cnt',  cnt)