# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(str, input())) for _ in range(N)]
#     arr_T = [list(row) for row in zip(*arr)]
#     list1 = []
#
#     for i in range(N):
#
#
arr = [
    [1, 2, 3, 4, 5, 6] ,
    [2,3,4,5,6,7]
    ]
for i in range(0,3):
    print(arr[0][i])











    # for i in range(N):
    #     for j in range(N-M+1):
    #         # print(arr[i][j+M-1], end = '') #=arr[i][j]
    #         # print(arr[i][j+M-2], end = '') #= arr[i][j+1]
    #         # print(arr[i][j+M-3], end = '')
    #         # print(arr[i][j+M-4], end = '')
    #         # print(arr[i][j+M-5])
    #         for k in range(M//2):
    #             if arr[i][j+M-1-k] == arr[i][j+k]:
    #                 list1.append(arr[i][j+k])
    #                 continue
    #             elif arr[i][j+M-1-k] != arr[i][j+k]:
    #                 break
    # for i in range(N):
    #     for j in range(N-M+1):
    #         # print(arr[i][j+M-1], end = '') #=arr[i][j]
    #         # print(arr[i][j+M-2], end = '') #= arr[i][j+1]
    #         # print(arr[i][j+M-3], end = '')
    #         # print(arr[i][j+M-4], end = '')
    #         # print(arr[i][j+M-5])
    #         for k in range(M//2):
    #             if arr_T[i][j+M-1-k] == arr_T[i][j+k]:
    #                 list1.append(arr_T[i][j+k])
    #                 continue
    #             elif arr_T[i][j+M-1-k] != arr_T[i][j+k]:
    #                 break






    #
    #
    #
    # print(arr_T)
    # print(list1)