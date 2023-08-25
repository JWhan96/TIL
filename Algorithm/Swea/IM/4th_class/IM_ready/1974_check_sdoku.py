from pprint import pprint
T = int(input())
for tc in range(1, T+1):
    N = 9
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_t = [list(i) for i in zip(*arr)]
    new_arr = []
    for i in range(0, N, 3):
        for j in range(0, N, 3):
            new_lst = []
            new_lst.extend(arr[i][j:j + 3])
            new_lst.extend(arr[i + 1][j:j + 3])
            new_lst.extend(arr[i + 2][j:j + 3])
            new_arr.append(new_lst)

    def Check():
        try:
            for i in range(N):
                for j in range(1,10):
                    arr[i].index(j)
                    arr_t[i].index(j)
                    new_arr[i].index(j)
            else:
                return 1
        except:
            return 0
    result = Check()
    print(f'#{tc} {result}')



    #
    #
    # pprint(arr)
    # print('########')
    # pprint(arr_t)
    # print('############')
    # pprint(new_arr)
    # print('*************')

# arr = [[7, 3, 6, 4, 2, 9, 5, 8, 1],
#        [5, 8, 9, 1, 6, 7, 3, 2, 4],
#        [2, 1, 4, 5, 8, 3, 6, 9, 7],
#        [8, 4, 7, 9, 3, 6, 1, 5, 2],
#        [1, 5, 3, 8, 4, 2, 9, 7, 6],
#        [9, 6, 2, 7, 5, 1, 8, 4, 3],
#        [4, 2, 1, 3, 9, 8, 7, 6, 5],
#        [3, 9, 5, 6, 7, 4, 2, 1, 8],
#        [6, 7, 8, 2, 1, 5, 4, 3, 9]]
# from pprint import pprint
# N = 9
# new_arr = []
# for i in range(0, N, 3):
#     for j in range(0, N, 3):
#         new_lst = []
#         new_lst.extend(arr[i][j:j+3])
#         new_lst.extend(arr[i+1][j:j+3])
#         new_lst.extend(arr[i+2][j:j+3])
#         new_arr.append(new_lst)

'''
[[7, 3, 6, 5, 8, 9, 2, 1, 4],
 [4, 2, 9, 1, 6, 7, 5, 8, 3],
 [5, 8, 1, 3, 2, 4, 6, 9, 7],
 [8, 4, 7, 1, 5, 3, 9, 6, 2],
 [9, 3, 6, 8, 4, 2, 7, 5, 1],
 [1, 5, 2, 9, 7, 6, 8, 4, 3],
 [4, 2, 1, 3, 9, 5, 6, 7, 8],
 [3, 9, 8, 6, 7, 4, 2, 1, 5],
 [7, 6, 5, 2, 1, 8, 4, 3, 9]]
 '''


