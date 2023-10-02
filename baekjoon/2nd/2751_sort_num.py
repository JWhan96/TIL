import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
lst = []
for i in range(N):
    lst.append(int(input()))
lst.sort()
for i in range(N):
    print(lst[i])

# def sol():
#     a=[None]*2000001
#     b=map(int,open(0))
#     next(b)
#     for i in b:a[i]=1
#     print("\n".join(str(i) for i in range(-1000000,1000001,1) if a[i]))
#
# sol()