# def dfs_stack(start):
#     visited = []
#     stack = [start]
#     while stack:
#         now = stack.pop()
#         # 이미 방문한 지점이라면 continue
#         if now in visited:
#             continue
#         # 방문하지 않은 지점이라면 방문 표시
#         visited.append(now)
#
#         for to in range(2, 0, -1):
#
#             next = arr[now-1][to]
#             # 방문한 지점이라면 stack에 추가하지 않음
#             if next in visited:
#                 continue
#
#             if arr[now][to] != -1:
#                 stack.append(next)
#     # 출력을 위한 반환
#     return visited
#
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# start = arr[0][0]
# dfs1 = []
# dfs2 = []
# dfs3 = []
# dfs_stack(start)

tree = [[-1, -1] for _ in range(1001)]
N = 0
preorder = []
inorder = []
postorder = []

def dfs(now):
    # now = -1이면 장식이 없는 경우 return
    if now == -1:
        return
    #전위 순회(루트 ->왼쪽 -> 오른쪽)
    preorder.append(now)
    #왼쪽으로 탐색
    dfs(tree[now][0])
    #중위순회(왼쪽 루트 오른쪽)
    inorder.append(now)
    #오른쪽으로 탐색
    dfs(tree[now][1])
    #후위순회(왼 오 루트)
    postorder.append(now)

N = int(input())
for _ in range(N): #장식 정보
    root, left, right = map(int, input().split())
    tree[root][0] = left
    tree[root][1] = right
dfs(1)
print(' '.join(map(str, inorder)))   #1
print(' '.join(map(str, preorder)))  #2
print(' '.join(map(str, postorder))) #3