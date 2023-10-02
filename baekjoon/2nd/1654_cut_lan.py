# K = 가지고 있는 랜선의 개수, N = 필요한 랜선의 개수
K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]
start, end = 1, max(arr)  # 이분탐색 처음과 끝위치

while start <= end:  # 적절한 랜선의 길이를 찾는 알고리즘
    mid = (start + end) // 2  # 중간 위치
    lines = 0  # 랜선 수
    for i in arr:
        lines += i // mid  # 분할 된 랜선 수

    if lines >= N:  # 랜선의 개수가 분기점
        start = mid + 1
    else:
        end = mid - 1
print(end)