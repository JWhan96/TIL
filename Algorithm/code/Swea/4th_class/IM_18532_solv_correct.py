T= int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ans = input().split()
    scores = []
    for _ in range(N):
        bonus = 1
        score = 0
        r = input().split()
        for i in range(M):
            if ans[i] == r[i]:
                score += bonus
                bonus += 1
            else:
                bonus = 1
        scores.append(score)
    result = max(scores) - min(scores)
    print(f'#{tc} {result}')