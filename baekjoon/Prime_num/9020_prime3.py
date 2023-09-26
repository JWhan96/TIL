def prime_list(M):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * (M)

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(M ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, M, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, M) if sieve[i] == True]

T = int(input())
for i in range(T):
    M = int(input())
    lst = prime_list(M)
    N = len(lst)
    i = 0
    j = 0
    result = []
    dict = {'res': (float('inf'), 0)}
    while True:
        # 넘어가면 continue
        if i == N:
            break
        if j == N:
            i += 1
            j = i
            continue

        if (lst[i] + lst[j]) > M:
            i += 1
            j = i
            continue
        if (lst[i]+ lst[j]) == M:
            result.append((lst[i], lst[j]))
            if abs(lst[i] - lst[j]) < abs(dict['res'][1]-dict['res'][0]):
                dict['res'] = (lst[i] , lst[j])
            if dict['res'][0] == dict['res'][1]:
                break
            j += 1
            # break
        else:
            j += 1

    print(*dict['res'])


# def is_prime(n):
#   if n == 1:
#     return False
#   for j in range(2, int(n ** 0.5) + 1):
#     if n % j == 0:
#       return False
#   return True
#
#
# for _ in range(int(input())):
#   num = int(input())
#
#   a, b = num // 2, num // 2
#   while a > 0:
#     if is_prime(a) and is_prime(b):
#       print(a, b)
#       break
#     else:
#       a -= 1
#       b += 1
