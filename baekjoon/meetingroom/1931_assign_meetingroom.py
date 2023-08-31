N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = []

arr.sort(key = lambda x: x[0])
arr.sort(key = lambda x: x[1])

# 시작지점은 맨 처음 요소
cnt = 1
curr = arr[0][1]

for j in range(1, len(arr)):
    #시작시간이 현재 회의의 끝나는 시간 이상이라면 cnt++, curr 교체
    if arr[j][0]  >= curr:
        cnt += 1
        curr = arr[j][1]
        continue

print(cnt)
