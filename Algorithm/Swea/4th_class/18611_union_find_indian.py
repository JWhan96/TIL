def find(node):
    if node != root[node]:            # 노드의 부모가 자기 자신이 아니라면
        root[node] = find(root[node]) # 부모 노드를 찾아가며 경로 압축
    return root[node]                 # 노드의 부모를 반환

def union(x, y):
    root_x = find(x)                      # x의 루트 부모 find
    root_y = find(y)                      # y의 루트 부모 find
    if root_x == root_y: # 입력 받은 두 인디언이 이미 같은 팀인경우, 명령을 무시합니다.
        return
    if rank[root_x] > rank[root_y]:           # x의 랭크가 더 크다면
        root[root_y] = root_x                 # y의 부모를 x의 루트 부모로 설정
    else:
        root[root_x] = root_y                 # 그렇지 않으면 x의 부모를 y의 루트 부모로 설정.
        if rank[root_x] == rank[root_y]:      # 만약 랭크가 같다면
            rank[root_y] += 1             # y의 랭크를 증가
N = int(input())
rank = [0] * 26
root = [i for i in range(26)]
for _ in range(N):
    a, b = input().split() # 연결할 두 인디언의 닉네임 입력
    union(ord(a) - 65, ord(b) - 65) # 닉네임을 숫자로 바꾸고 연결
#모든 노드의 루트 찾기
for i in range(26):
    find(i)
DAT = [0] * 26
team = 0
for i in range(26):
    DAT[root[i]] += 1 #각 루트별 노드 개수 세기
team = 0
indi = 0
for data in DAT:
    if data > 1: #노드의 개수가 2개이상이면 팀
        team += 1
    elif data == 1: #노드의 개수가 1개면 개인 연주자
        indi += 1
print(team)
print(indi)