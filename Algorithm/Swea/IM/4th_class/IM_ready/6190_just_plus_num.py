T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    multiple = []
    for i in range(0, N):
        for j in range(N-1, i, -1):
            multiple.append(str(arr[i] * arr[j]))

    lst = []

    for i in range(len(multiple)):
        for j in range(len((multiple[i]))-1):
            if multiple[i][j] > multiple[i][j+1]:
                break
        else:
            lst.append(int(multiple[i]))

    if lst:
        result = max(lst)

        print(f'#{tc} {result}')
    else:
        print(f'#{tc} {-1}')
