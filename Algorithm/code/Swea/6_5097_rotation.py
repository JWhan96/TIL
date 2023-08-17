def enQ(arr):
    arr.append(arr[0])

def deQ(arr):
    arr.pop(0)

def Rotation(arr):
    for i in range(M):
        enQ(arr)
        deQ(arr)

    return arr
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    result = Rotation(arr)
    print(f'#{tc} {result[0]}')

