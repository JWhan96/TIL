T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) #N: 학생수, M: 문제수
    sol = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    score = []

    for i in range(N):
        cnt = 0
        bonus = 0
        for j in range(0, M):
            if arr[i][j] == sol[j]:
                cnt += 1 + bonus
                bonus += 1
            if j+1 < M and arr[i][j+1] != sol[j+1]:
                bonus = 0
        score.append(cnt)
    max_v = (max(score))
    min_v = (min(score))
    print(f'#{tc} {max_v-min_v}')










# T= int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     ans = input().split()
#     scores = []
#     for _ in range(N):
#         bonus = 1
#         score = 0
#         r = input().split()
#         for i in range(M):
#             if ans[i] == r[i]:
#                 score += bonus
#                 bonus += 1
#             else:
#                 bonus = 1
#         scores.append(score)
#     result = max(scores) - min(scores)
#     print(f'#{tc} {result}')