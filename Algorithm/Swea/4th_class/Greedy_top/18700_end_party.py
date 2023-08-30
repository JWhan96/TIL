n, m = map(int, input().split())
six_min = float('inf')
one_min = float('inf')
for _ in range(m):
    six_cost, one_cost = map(int, input().split())
    #현재까지 가장 저렴한 6병세트와 낱개 가격 업데이트
    six_min = min(six_min, six_cost)
    one_min = min(one_min, one_cost)
if one_min * 6 < six_min: # 낱개로 사는것이 셑느로 사는것보다 저렴하다면 낱개로 구매
    print(one_min * n)
else:
    buy = n//6
    n %= 6 #6으로 나눈 나머지가 남은 병수
    if n* one_min > six_min: #낱개로 사는게 더 비싸면
        buy += 1
        print(buy * six_min)
    else: # 적절히 섞어서
        print(buy * six_min + one_min *n)
