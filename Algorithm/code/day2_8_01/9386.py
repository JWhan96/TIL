T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    # arr = list(input())
    list1 = []
    count = 0
    for i in arr:
        if i == 1:
            count += 1
        elif i == 0:
            if count != 0:
                list1.append(count)
            count = 0
    print(list1)
