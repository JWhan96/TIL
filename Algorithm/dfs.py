# graph = {1: [2, 3], 2: [4, 5], 3: [6, 7], 4: [8, 9], 5: [-1, 10], 6: [-1, -1], 7: [11, -1], 8: [-1, -1], 9: [-1, -1], 10: [-1, -1], 11: [-1, -1]}
#
#
# visited = {}  # 방문한 노드를 기록하기 위한 딕셔너리
# inorder = []  # 중위 우선 탐색 경로를 저장하는 리스트
# preorder = []  # 선위 우선 탐색 경로를 저장하는 리스트
# postorder = []  # 후위 우선 탐색 경로를 저장하는 리스트
#
# def dfs(node):
#
#
#     if node not in visited:
#         visited[node] = True
#
#     # 선위 우선 탐색 (Pre-order)
#     preorder.append(node)
#
#     for neighbor in graph[node]:
#         if neighbor == -1:
#             continue
#         dfs(neighbor)
#
#     # # 중위 우선 탐색 (In-order)
#     # inorder.append(node)
#     #
#     # # 후위 우선 탐색 (Post-order)
#     # postorder.append(node)
#
#
# # DFS 시작 노드를 선택하여 호출
# start_node = 1
# dfs(start_node)
#
# # 경로 출력
#
# print("In-order:",(inorder))
# print("Pre-order:", (preorder))
# print("Post-order:",(postorder))

graph = {1: [2, 3], 2: [4, 5], 3: [6, 7], 4: [8, 9], 5: [-1, 10], 6: [-1, -1], 7: [11, -1], 8: [-1, -1], 9: [-1, -1],
         10: [-1, -1], 11: [-1, -1]}

visited = {}  # 방문한 노드를 기록하기 위한 딕셔너리
inorder = []  # 중위 우선 탐색 경로를 저장하는 리스트
preorder = []  # 선위 우선 탐색 경로를 저장하는 리스트
postorder = []  # 후위 우선 탐색 경로를 저장하는 리스트

v = []
def dfs(now):
    v.append(now)

    for nxt in graph[now]:
        if nxt == -1:
            continue
        if nxt in v:
            continue
        dfs(nxt)

dfs(1)
print(v)

n = 3
bit = [0] * n
def bitbit(i, n):   # 함수
    if i == n:      # 기저조건(끝내기)
        return 1
    for j in range(2):  # 반복
        bit[i] = j      #
        return bitbit(i+1, n)
bitbit(0, n)