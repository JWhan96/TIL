T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N+1)]
    for i in range(M):
        idx, value = map(int, input().split())
        tree[idx] = value # 트리에 리프 노트의 값을 저장
    for i in range(N, 0, -1): # 노드의 개수부터 1까지 역순
        if i//2 > 0 : #부모 노드의 인덱스가 0보다 크다면
            tree[i//2]  += tree[i] # 부모노드에 자식노드의 값을 더함
    result = tree[L]
    print(f'#{tc} {result}')