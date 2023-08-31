a, b = map(int, input().split())
cnt = 0

while b >= a:
    if b == a:
        print(cnt)
        exit()
    if b%2 == 1: # 1의 자리가 1인경우, 1제거
        b //= 10
    elif b % 2 == 0: # 짝수 인 경우 2로 나누기
        b//=2
    else: # 두조건 아닐때 b를 a로 바꾸는 것 불가
        print(-1)
        exit()
    cnt += 1 # 연산을 한번 수행했으므로 cnt ++

print(-1)