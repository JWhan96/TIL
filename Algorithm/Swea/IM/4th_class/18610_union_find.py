#Union 두그룹 하나로 합친다
#Find 특정노드가 어느 그룹에 속해있는지 찾는다

def find(node):
    if node != root[node]: # 노드의 부모가 자기 자신이 아니라면
        root[node] = find(root[node]) #부모노드를 찾아간다 -> 경로 압축 수행
    return root[node]

def union(x, y):
    root_x = find(x) #x의 루트 부모 찾기
    root_y = find(y) #y의 루트 부모 찾기
    if rank[root_x] > rank[root_y]:
        root[root_y] = root_x
    else:
        root[root_x] = root_y
        if rank[root_x] == rank[root_y]:
            rank[root_y] += 1

N,Q = map(int, input().split())
rank = [0] * (N+1) #각 노드의 랭크를 저장하는 리스트
root = [i for i in range(N+1)] # 각 노드의 루트 부모를 저장하는 리스트
for _ in range(Q):
    K, A, B = map(int, input().split())
    if K == 0:
        if find(A) == find(B): #A와 B가 같은 그룹에 속하면
            print('YES')
        else:
            print('NO')
    else:
        union(A, B) #A와 B를 같은 그룹으로 연결