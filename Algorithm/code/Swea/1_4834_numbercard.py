T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    count = [0] * (max(arr)+1)
    for i in range(len(arr)):
        count[arr[i]] += 1


    count_v = 0
    index_v = 0
    for i in range(len(count)):

        if count_v <= count[i]:
            count_v = count[i]
            index_v = i
    print(f'#{tc} {index_v} {count_v}')