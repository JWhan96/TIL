def sub_tree(node): #서브트리의 노드의 수를 찾는 함수
    global cnt
    for i in range(2): #왼쪽 자식, 오른쪽 자식
        if tree[i][node]: #해당 노드의 자식이 있다면
            cnt += 1
            n = tree[i][node] # 자식 노드의 번호
            sub_tree(n) #자식노드에 대해 재귀호출
T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    temp = input().split()
    # 노드 번호는 1번부터 E+1번 까지 존재 -> 이진트리 리스트 초기화
    tree = [[0 for _ in range(E+1)] for _ in range(2)]
    for i in range(E):
        p_node = int(temp[2*i]) # 부모노드번호 ->짝수 번째
        c_node = int(temp[2*i+1]) # 자식노드번호 -> 홀수 번째
        if tree[0][p_node] == 0: # 왼쪽 자식이 없다면 할당, 왼쪽 자식이 있다면 오른쪽에 할당
            tree[0][p_node] = c_node
        else:
             tree[1][p_node] = c_node
    cnt = 1
    sub_tree(N)
    print(f'#{tc} {cnt}')