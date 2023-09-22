def find(node):
    if parents[node] == node:
        return node
    parents[node] = find(parents[node])
    return parents[node]

def union(a, b):
    pa = find(a)
    pb = find(b)

    if pa > pb:
        pa, pb = pb, pa

    parents[pb] = pa

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 딕셔너리 컴프리헨션: 각 사람에 대해 초기에는 자기 자신을 부모로 설정
    parents = {i: i for i in range(1, N+1)}
    for i in range(M):
        a, b = map(int, input().split())
        # 두 사람이 다른 그룹에 속해있다면 union 실행
        if find(a) != find(b):
            union(a, b)
    group = set()
    for i in range(1, N+1):
        # 해당 사람이 그룹에 속해있지 않다면 해당 사람의 최종 그룹을 찾아 set에 추가
        if parents[i] not in group:
            x = find(i)
            if x not in group:
                group.add(x)
    print(f'#{tc} {len(group)}')