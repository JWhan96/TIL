n, target = map(int, input().split())
arr = list(map(int, input().split()))
cnt= 0
sum = 0
low, high = 0,0
while True:
    if sum >= target or high ==n:
        sum -= arr[low]
        low += 1
    elif sum < target:
        sum += arr[high]
        high += 1
    if sum == target:
        cnt += 1
    if low == n:
        break
print(cnt)