## 고지식한 패턴 검색

t = 'This is a book~!'
p = 'is'
N = len(t)
M = len(p)

def BruteForce(p, t):
    i = 0 #t의 인덱스
    j = 0 #p의 인덱스
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j= -1
        i = i+1
        j = j+1
    if j ==M : return i -M  #검색성공
    else: return -1 #검색실패

print(BruteForce(p,t))



#
# #####KMP 알고리즘
# def kmp(t, p):
#     N = len(t)
#     M = len(p)
#     lps = [0] * (M+1)
#
#     j = 0
#     lps[0] = -1
#     for i in range(1, M):
#         lps[i] = j
#         if p[i] == p[j]:
#             j += 1
#     else:
#         j = 0
#     lps[M] = j
#     print(lps)
#
#     i = 0
#     j = 0
#     while i < N and j <= M:
#         if j == -1 or t[i] == p[j]:
#             i += 1
#             j += 1
#         else:
#             j = lps[j]
#         if j == M:
#             print(i-M, end = ' ')
#             j = lps[j]
#     print()
#     return
#
# t = 'zzzabcdabcdabcefabcd'
# p = 'abcdabcef'
# kmp(t, p)
# t = 'AABAACAADAABAABA'
# p = 'AABA'
# kmp(t, p)
# t = 'AAAAABAAABA'
# p = 'AAAA'
# kmp(t, p)
# t = 'AAAAABAAABA'
# p = 'AA'
# kmp(t, p)