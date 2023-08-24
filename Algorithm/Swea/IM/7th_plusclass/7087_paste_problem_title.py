#65~90
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    title = []
    for i in range(65, 91):
        title.append(chr(i))

    arr = [list(input()) for _ in range(N)]
    count = 0
    for i in range(N):
        if title[0] == arr[i][0]:
            title.pop(0)
            count += 1
    print(f'#{tc} {count}')

