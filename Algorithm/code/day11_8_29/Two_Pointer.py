'''
1부터 10000사이의 n개의 자연수 중에서 연속된 숫자를 더했을때 합이 m이 되는 경우는 몇가지?
(투포인터 -> 구간의 크기가 정해지지 x)
input
10 5
1 2 3 4 2 5 3 1 1 2

output
3
'''
n, target= map(int, input().split())
arr = list(map(int, input().split()))
cnt, sum = 0, 0
#투포인터 high, low
high, low = 0, 0
while True:
    if sum >= target or high == n: # 합이 타겟보다 크거나 같다면(범위 줄이기)
        sum -= arr[low]
        low += 1
    elif  sum < target: #합이 타겟보다 작다면 (범위 넓히기)
        sum += arr[high]
        high += 1
    if sum == target:
        cnt += 1
    if low == n:
        break
print(cnt)
