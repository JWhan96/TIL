'''
1 2 4 4
2 3 5 7
3 1 6 5
7 3 8 6
'''
arr = {}
for _ in range(4):
    rx, ry, cx, cy = map(int, input().split())
    for i in range(rx, cx):
        for j in range(ry, cy):
            arr[(i,j)] = 1
print(len(arr))


