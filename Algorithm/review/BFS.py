arr = [
    [0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1],
    [0, 0, 1, 1, 0, 0]
       ]
N = int(input())  # 시작 노드

def BFS(N, n, arr):
    visited = [0] * n  # 방문여부 행렬
    queue = []
    queue.append(N)    # 시작노드 큐에 추가
    visited[N] = 1     # 시작노드 방문 표시
    while queue:  # 큐추가/팝 반복하며 모든 요소 탐색할 때까지(큐가 빌 때까지)
        t = queue.pop(0)  # 첫 인덱스 요소 pop(큐 특성/선입선출)
        print(t)
        for i in range(6):
            if arr[t][i] == 1 and visited[i] == 0:  # 간선이 있고 방문한적이 없는 노드라면
                queue.append(i)  # 큐에 추가
                visited[i] = 1
BFS(N, 6, arr)