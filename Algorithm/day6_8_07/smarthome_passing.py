#코코가 개발한 코드생성기
# 1. 랜덤으로 N개 길이의 Sample이 주어진다
# 2. 그리고 K개 길이의 Passcode가 주어진다
# 3. 사용자는 Sample 에서 Passcode 를 '순차적으로' 만들수 있는지 검증한다

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))

    # cnt = 0
    # result = 0
    # for i in range(N):
    #     if passcode[cnt] == sample[i]:
    #         cnt += 1
    #     if cnt == K:
    #         result = 1
    #         break
    # print(f'#{tc} {result}')

    indexes = []
    result = 1

    for i in range(K):
        now = passcode[i]
        try:
            index = sample.index(now)
            sample = sample[index+1:]
        except:
            result = 0

    print(result)