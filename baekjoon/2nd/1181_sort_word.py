import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
lst = []
for i in range(N):
    lst.append(input().rstrip())
st = set(lst)
lst1 = list(st)
lst1.sort(key = lambda x: x)
lst1.sort(key= lambda x: len(x))
for i in range(len(lst1)):
    print(lst1[i])


