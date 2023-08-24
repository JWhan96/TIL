'''
입력
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
7 4
1 6
2 3
2 6
3 5
2 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9

출력
#1 1
#2 1
#3 1
'''
T = int(input())

def DFS(start, end):
    stack = []
    visited = [False] * (V + 1)
    stack.append(start)  # 시작점을 스택에 넣음
    while stack:  # 스택이 비어있으면 반복문 종료
        now = stack.pop()  # 스택의 마지막 노드를 꺼냄
        visited[now] = True  # 현재 노드를 방문
        for next in range(1, V+1):
            if node[now][next] and not visited[next]: #  방문하지 않았고 열결되어 있다면
                stack.append(next)  # 스택에 추가
    if visited[end]:  # 끝점에 방문했다면
        return 1
    else:
        return 0

for tc in range(1, T+1):
    V, E = map(int, input().split())  # 노드와, 간선의 개수
    node = [[0 for _ in range(V+1)] for _ in range(V+1)]  # 인접행렬 초기화
    for _ in range(E):
        start, end = map(int, input().split())
        node[start][end] = 1 # 해당 인접행렬에 1할당 -> 연결됨
    S, G = map(int, input().split())
    print(f'#{tc} {DFS(S, G)}')
