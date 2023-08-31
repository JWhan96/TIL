T = int(input())
for tc in range(1, T+1):
    N = int(input())
    I = [list(map(int, input().split())) for _ in range(N)]
    result = []

    #그리디의 핵심은 정렬!
    #회의 시작시간 정렬 후 회의 끝 시간 정렬
    I.sort(key = lambda x: x[0])
    I.sort(key = lambda x: x[1])

    # 시작지점은 맨 처음 요소
    cnt = 1
    curr = I[0][1]

    for j in range(1, len(I)):
        #시작시간이 현재 회의의 끝나는 시간 이상이라면 cnt++, curr 교체
        if I[j][0]  >= curr:
            cnt += 1
            curr = I[j][1]
            continue

    print(f'#{tc} {cnt}')
