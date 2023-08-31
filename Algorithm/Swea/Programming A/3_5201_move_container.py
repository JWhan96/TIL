T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cont = list(map(int, input().split()))
    car = list(map(int, input().split()))

    result = 0
    while cont and car:
        max_cont = max(cont)
        max_car = max(car)
        idx_cont = cont.index(max_cont)
        idx_car = car.index(max_car)
        if max_cont > max_car:
            cont.pop(idx_cont)
        if max_cont <= max_car:
            weight = cont.pop(idx_cont)
            car.pop(idx_car)
            result += weight
    print(f'#{tc} {result}')

# sort사용해서 하면 시간이 늘어나서 런타임 에러