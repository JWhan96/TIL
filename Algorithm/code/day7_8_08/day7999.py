## 고지식한 패턴 검색

n = 'Thid is a book~!'
m = 'is'
N = len(n)
M = len(m)

def BruteForce(n, m):
    d = 1
    n_index = 0 #n의 인덱스
    m_index = 0 #m의 인덱스
    while m_index < M and n_index < N:
        if n[n_index] != m[m_index]:
            n_index = n_index - m_index + 1
            m_index = -1
        n_index = n_index + 1
        m_index = m_index + 1
    if m_index == M :
        return n_index - M  #검색성공

    else:
        return -1 #검색실패

print(BruteForce(n,m))



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