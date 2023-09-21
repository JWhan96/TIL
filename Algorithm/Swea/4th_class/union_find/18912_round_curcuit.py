'''
5
0 0 0 1 0
0 0 1 0 0
0 1 0 1 1
1 0 1 0 1
0 0 1 1 0

4
0 1 0 0
1 0 1 0
0 1 0 1
0 0 1 0
'''

def find_set(x):
    if parents[x] == x:
        return x
    
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return
    
    if x < y:
        parents[y] = x
    else:
        parents[x] = y
    

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
parents = [i for i in range(N)]

for i in range(N):
    for j in range(i+1, N):    
        
        if find_set(i) == find_set(j):   
            print('WARNING')
            exit()
        if arr[i][j] == 1:
            union(i, j)    
else:
    print('STABLE')
        


# for i in range(N):
#     for j in range(i+1, N):
#     # for j in range(N):
#         if arr[i][j] == 0:
#             continue
#         if find_set(i) == find_set(j):
#             print('WARNING')
#             exit()
#         union(i, j)
# print('STABLE')








