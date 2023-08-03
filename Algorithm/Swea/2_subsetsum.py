T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    ###########
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n = len(arr)
    list1 = []
    count = 0

    for i in range(1 << n):
        list2 = []
        for j in range(n):
            if i & (1 << j):
                list2.append(arr[j])

        list1.append(list2)
    for i in list1:
        if (len(i)==N) & (sum(i)==K):
            count += 1

    print(f'#{tc} {count}')

    ######강사님 코드
    arr = [i for i in range(1, 13)]
    result = 0
    #1<<12 -> 이진수 1을 왼쪽으로 12비트 이동 -> 100000000000 -> 2**12
    for i in range(1 << 12):
        sum_sub = 0
        subset = []
        for j in range(12):
            # i의 j번째 비트가 1인지 아닌지 알수 있다.
            # 12의 이진수 1100, 5의 이진수 0101 -> 1100 & 0101 -> 0100 -> 같은 위치의 비트가 둘다 1인것만 반환
            if i & (1 << j):
                sum_sub += arr[j]
                subset.append(arr[j])
        if len(subset) == N and sum_sub ==K:
            result += 1
    print(f'#{tc} {result}')