'''
입력
첫번째 줄에는 테스트 케이스 T가 주어진다
두번째 줄부터 각 테스트 케이스가 주어진다
각 테스트 케이스와 첫번째 줄에는 Sample의 길이 N, passcode의 길이 K가 주어진다
각 테스트 케이스의 두번째 줄에는 N의 길이의 Sample이 공백으로
각 테스트 케이스의 세번째 줄에는 K의 길이의 Passcode가 공백으리ㅗ
공백으로 주어지는 값은 0~9이다

입력
2
10 4
1 1 2 2 3 3 4 4 5 5
1 2 3 4
7 4
1 2 2 4 3 3 4
4 3 2 1

출력

'''



#코코가 개발한 코드생성기
# 1. 랜덤으로 N개 길이의 Sample이 주어진다
# 2. 그리고 K개 길이의 Passcode가 주어진다
# 3. 사용자는 Sample 에서 Passcode 를 '순차적으로' 만들수 있는지 검증한다

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))
    print(f'sample = {sample}')
    print(f'passcode = {passcode}')
    cnt = 0

    result = 0
    for i in range(N):
        if passcode[cnt] == sample[i]:
            cnt += 1
        if cnt == K:
            result = 1
            break
    print(f'#{tc} {result}')

    # indexes = []
    # result = 1

    # for i in range(K):
    #     now = passcode[i]
    #     try:
    #         index = sample.index(now)
    #         sample = sample[index+1:]
    #     except:
    #         result = 0
    #
    # print(result)