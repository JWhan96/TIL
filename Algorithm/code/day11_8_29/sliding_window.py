'''
input
10 2
3 -2 -4 -9 0 3 7 13 8 -3

output
21
'''
N, M = map(int, input().split())
arr = list(map(int, input().split()))
sum = 0
for i in range(M): #  처음 첫 M개의 구간의 합 구하기
    sum += arr[i]
    max_v = sum
for j in range(N-M):
    sum += arr[j+M]
    sum -= arr[j]
    if sum > max_v:
        max_v = sum

print(max_v)

