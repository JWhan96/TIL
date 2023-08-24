T = 10
for tc in range(1, T+1):
    N = int(input())

    arr = list(map(int, input().split()))
    for _ in range(N):

        arr[arr.index(max(arr))] -= 1
        arr[arr.index(min(arr))] += 1
    result = max(arr) - min(arr)
    print(f'#{tc} {result}')

