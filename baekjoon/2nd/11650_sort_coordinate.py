import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
lst = []
for i in range(N):
    lst.append(list(map(int, input().split())))

lst.sort(key = lambda x: x[1])
lst.sort(key = lambda x: x[0])
for i in lst:
    print(*i)