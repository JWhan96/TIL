# 큐 : 선입선출
# 우선순위 큐: 데이터들 우선순위를 가지고 저장, 우선순위가 높은 것부터 꺼냄
# 힙: 우선순위 큐를 구현하는 트리기반의 자료구조, 최대힙, 최소힙
# import heapq -> heapq 라이브러리를 사용하여 최소 힙 구현
# heapq.heappush(heap, num) : num을 최소힙 heap에 삽입
# heapq.heappop(heap) : 최소힙, heap에서 가장 작은 값을 꺼내서 반환

import heapq
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = []
    number = map(int, input().split())

    for num in number:
        heapq.heappush(tree, num) # 힙에 num을 추가 -> 자동으로 정렬

    sum_v = 0
    N = len(tree) // 2 #부모의 노드 인덱스 계산

    while N:
        sum_v += tree[N-1]
        N //= 2 # 부모 노드로 올라가기 위해 N//2

    print(f'#{tc} {sum_v}')
