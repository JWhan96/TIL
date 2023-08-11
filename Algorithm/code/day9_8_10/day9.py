# #피보나치 재귀이용
# def fibo(n):
#     global cnt
#     global memo

#     cnt += 1
#     if n<2:
#         return memo[n]
#     else:
#         if memo[n] == 0:
#             memo[n] = fibo(n-1) + fibo(n-2)
#         return memo[n]
# N= 30
# memo = [0] * (N+1)
# memo[0] = 0
# memo[1] = 1
# cnt = 0
# print(fibo(N), cnt)

# ## 피보나치 dp이용
# def fibo(n):
#     dp = [0] * (n+1)
#     dp[0] = 0
#     dp[1] = 1
#     for i in range(2, n+1):
#         dp[i] = dp[i-1] + dp[i-2]
#     return dp[n]

# print(fibo(100))

## DFS 연습문제 3
'''
V E
v1, w1, v2, w2 ...
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

V, E = map(int, input().split()) #1번부터 V번 정점, 
arr = list(map(int, input().split()))
adj_m = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1

def dfs(n, V, adj_m):
    stack = []  #stack 생성
    visited = [0] * (V+1) #방문점 생성
    visited[n] = 1 #시작점 방문 표시
    print(n)  
    while True:
        for w in range(1, V+1): # 현재 정점 n에 인접하고 미방문 w 찾기 
            if adj_m[n][w] == 1 and visited[w] ==0:
                stack.append(n) 
                n = w  #새로 옮겨갈 위치 w
                print(n)
                visited[n] = 1 # w 방문 표시
                break # for w,n에 인접인 c찾은경우
        else: 
            if stack: #스택에 지나온 정점이 남아있으면
                n = stack.pop() #pop해서 다른 w찾을 준비
            else: #스택이 비어있으면
                break #탐색끝
    return



dfs(1, V, adj_m)