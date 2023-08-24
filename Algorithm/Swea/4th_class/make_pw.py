def Password(arr):

    while True :
        idx = 0
        #한사이클
        for i in range(5):
            idx += 1
            arr.append(arr.pop(0) - idx)
            # 사이클 도는 도중 마지막 인덱스가 0혹은 0이하가 되면 0으로 바꾼 후 반환
            if arr[-1] <= 0:
                # (arr.pop(-1))
                # arr.append(0)
                arr[-1] = 0
                return arr
    return
for i in range(10):
    T= int(input())
    arr = list(map(int, input().split()))

    Password(arr)
    print(f'#{T}', end = ' ')
    print(*arr)
