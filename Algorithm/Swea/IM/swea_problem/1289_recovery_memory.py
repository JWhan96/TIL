'''
2
0011
100

'''
T = int(input())
for tc in range(1, T + 1):
    num1 = list(input())
    N = len(num1)
    num2 = ['0'] * len(num1)
    count = 0
    for i in range(N):
        if num1[i] != num2[i]:
            if num2[i] == '0':
                num2[i:N] = ['1'] * (N-i)
                count += 1
            elif num2[i] == '1':
                num2[i:N] = ['0'] * (N - i)
                count += 1
    print(f'#{tc} {count}')

##############################
# T = int(input())
# for tc in range(1, T + 1):
#     num1 = list(input())
#     N = len(num1)
#     # print(num1)
#     num11 = ''.join(num1)
#     num2 = ['0'] * len(num1)
#     # print(num2)
#     index1 = 0
#     if '1' in num1:
#         for i in range(N):
#             if num1[i] == '1':
#                 index1 = i
#                 break
#
#     index_count = 0
#     count = 0
#     while index_count + index1 != N:
#         num21 = ''.join(num2)
#         if num21 == num11:
#             break
#         # print(num2, num1)
#         if num1[index1 + index_count] == "1":
#             num2[index1 + index_count:N] = ['1'] * (N - index1 - index_count)
#             index_count += 1
#             count += 1
#
#         elif num1[index1 + index_count] == "0":
#             num2[index1 + index_count:N] = ['0'] * (N - index1 - index_count)
#             index_count += 1
#             count += 1
#
#         num21 = ''.join(num2)
#
#         if num21 == num11:
#             break
#
#         while num1[index1 + index_count] == num2[index1 + index_count]:
#             index_count += 1
#
#     print(f'#{tc} {count}')

####
