def binary_search(target):
    start, end = 0, N #시작점 끝점 초기화
    while start <= end:
        mid = (start + end) // 2
        #1. 왼쪽 부분 탐색, 중간점의 값이 찾고자 하는 값보다 큰 경우
        if A[mid] > target:
            end = mid - 1
        #2. 오른쪽 부분 탐색, 중간점의 값이 찾고자 하는 값보다 작은 경우
        elif A[mid] < target:
            start = mid + 1
        #3. 탐색 종료. 중간점의 값이 찾고자 하는 값과 같은경우
        elif A[mid] == target:
            return True
    return False #탐색이 종료 되었는데도 찾지 못한 경우
N = int(input())
A = tuple(sorted(list(map(int, input().split()))))
K = int(input())
B = tuple(map(int, input().split()))
for b in B:
    if binary_search(b):
        print('O', end = '')
    else:
        print('X', end = '')