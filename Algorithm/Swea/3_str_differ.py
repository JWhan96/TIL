T = int(input())
for tc in range(1, T+1):
    N = str(input())
    M = str(input())
    result = 0
    if N in M:
        result += 1
    else:
        result = 0
    print(f'#{tc} {result}')