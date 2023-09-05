T = int(input())
for tc in range(1, T+1):
    arr = list(input())
    bonus = 0
    cnt = 0
    for i in range(len(arr)):
        if arr[i] == 'O':
            cnt += 1 + bonus
            bonus += 1
        if arr[i] =='X':
            bonus = 0
    print(cnt)