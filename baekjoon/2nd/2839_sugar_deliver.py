
N = int(input())
cnt = 0 # 5의 몫의 개수

bas = float('inf') # 바구니 개수

while True:

    result = float('inf')
    if cnt == ((N//5) +1):
        break
    if N - (5*cnt) < 0:
        cnt += 1
    else:
        if (N - (5*cnt))% 3 == 0:
            result = (((N - (5*cnt))// 3)+ cnt)
            if result < bas:
                bas = result
            cnt += 1
        else:
            cnt += 1
            continue

if bas == float('inf'):
    print(-1)
else:
    print(bas)
