#부모 노드 찾는 함수
def find(node):
    #자기 자신이 부모 노드가 아니라면, 부모노드를 찾아간다
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

#두 노드를 연결하는 함수
def union(a, b):
    pa = find(a)
    pb = find(b)
    if pa < pb: # 작은 번호의 부모를 기준으로 합치기
        parent[pb] = parent[pa]
    else:
        parent[pa] = parent[pb]

T = int(input())
for tc in range(1, T + 1):
    v, e = map(int, input().split()) #노드의 개수v, 간선이 개수 e
    # 가중치를 기준으로 정렬(lambda 함수)
    eges = sorted([list(map(int, input().split())) for _ in range(e)], key = lambda x : x[2])
    parent = [i for i in range(v + 1)] #각 노드의 초기 부모노드는 자기 자신
    total_v = 0 #최소 가중치의 합
    cnt = 0

    for i in range(e): #모든 간선에 대해 순회
        if cnt == v: #모든 노드가 연결되면 break
            break
        s, e, w = eges[i] #간선의 시작노드, 끝 노드, 가중치
        if find(s) == find(e): #시작 노드와 끝 노드의 부모가 같으면 continue
            continue
        union(s, e)
        total_v += w #가중치의 합 갱신
    print(f'#{tc} {total_v}')
