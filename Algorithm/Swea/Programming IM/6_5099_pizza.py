T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    pizza = [[i + 1, p] for i, p in enumerate(arr)]
    queue = []
    queue.append(pizza.pop(0))

    while queue:
        while len(queue) != N and pizza:

            queue.append(pizza.pop(0))

        if len(queue) > 1:
            t = queue.pop(0)
            if t[1] != 0:
                t[1] //= 2
                if t[1] != 0:
                    queue.append(t)


        else:
            result = queue.pop(0)
            print(f'#{tc} {result[0]}')
            break




















####
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     cheeses = list(map(int, input().split()))
#
#     pizzas = [[i+1, p] for i, p in enumerate(cheeses)]
#     oven = pizzas[:N] #화덕에 처음들어가는 피자
#     remain = pizzas[N:] #남은피자
#
#     while len(oven) >1:
#          now = oven.pop(0)
#          #now[0] : 현재 피자의 인덱스, now[1]: 현재치즈양
#          now[1]  //=  2
#          if now[1] == 0:
#              if remain:
#                  oven.append(remain.pop(0))
#          else: #치즈가 다 안녹았다면
#              oven.append(now)
#     print(f'#{tc} {oven[0][0]}')