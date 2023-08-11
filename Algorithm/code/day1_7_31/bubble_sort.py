def BubbleSort(a, N):            # 정렬할 List, N 원소 수
    for i in range(N-1, 0, -1):  # 범위의 끝 위치
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]