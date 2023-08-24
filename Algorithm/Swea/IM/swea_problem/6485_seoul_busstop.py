T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = [0] * 5001
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            cnt[i] += 1
    P = int(input())
    c_list = [int(input()) for _ in range(P)]
    result = [cnt[k] for k in c_list]
    print(f'#{tc}', *result)


#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     a_list = []
#     b_list = []
#     for i in range(N):
#         a, b = map(int, input().split())
#         a_list.append(a)
#         b_list.append(b)
#
#     P = int(input())
#     c_list = []
#
#     for j in range(P):
#         c = int(input())
#         c_list.append(c)
#
#     count_list = [0] * 5001
#
#     for i in range(len(a_list)):
#         count = 0
#         count = a_list[i]
#         for j in range((b_list[i] + 1) - a_list[i]):
#             count_list[count] += 1
#             count += 1
#
#     result = []
#     for k in c_list:
#         result.append(count_list[k])
#     print(f'#{tc}', *result)
