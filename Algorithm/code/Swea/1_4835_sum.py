T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    max_v = 0
    min_v = sum(arr)
    listM = [i for i in range(M)]

    for i in range(N-M+1):
        cnt = 0
        for j in listM:
            cnt += arr[i+j]
        if max_v < cnt:
            max_v = cnt
        if min_v > cnt:
            min_v = cnt
    print(f'#{tc} {max_v - min_v}')