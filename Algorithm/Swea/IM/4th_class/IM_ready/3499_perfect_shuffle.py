T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(input().split())

    if N %2 ==1:
        after = arr[N//2+1:]
        before = arr[:N//2+1]
    else:
        after = arr[N//2:]
        before= arr[:N//2]
    index = 0

    for i in range(1, len(before)+1):
        try:
            before.insert(i+index, after[i-1])
            index += 1
        except:
            break

    print(f'#{tc}', *before)

