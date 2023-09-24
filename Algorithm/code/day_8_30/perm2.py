def perm(i, N, K): # i는 이전에 고른 개수, N개에서 K개를 고르는 순열
    global cnt
    if i == K: # 순열 완성 : K를 모두 고른 경우
        cnt += 1
        print(cnt, p)
        return
    else:
        for j in range(N): # p[i]에 들어갈 숫자를 결정
            if used[j] == 0: # 아직 사용되기 전이라면
                p[i] = card[j]
                used[j] = 1
                perm(i + 1, N, K)
                used[j] = 0

card = [1, 2, 3, 4, 5]
N = 5 # N개의 카드에서
K = 3 # K개를 뽑아 만드는 순열
used = [0] * N #사용한 카드인지 표시하는 리스트
p = [0] * K
cnt = 0
perm(0, N, K)





















