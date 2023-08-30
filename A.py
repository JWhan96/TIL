# for i in range(N):
#     for j in range(i+1, N):
#         for k in range(j+1, N):
#             print(lst[i], lst[j], lst[k])
#             print()
######





T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    people = list(map(int, input().split()))
    def area():
        lst = []
        for i in range(N):
            lst.append(i)

        sub_N = []  # 처음 그룹 나누는 기준 2덩이로
        for i in range(1, N):
            a = i
            b = N - i
            if a <= b:
                sub_N.append(a)
        # print(sub_N)
        # sub_N = [1 ,2, 3, 4]
        result = 23e6
        for i in sub_N:  ###A그룹 B그룹 나누는 법
            A_group = []
            B_group = []
            ##
            if i == 1:

                for i in range(N):
                    copylst = lst[:]
                    a_lst = []
                    a_lst.append(copylst.pop(i))
                    if not a_lst in B_group:
                        A_group.append(a_lst)
                        B_group.append(copylst)
            elif i == 2:

                for i in range(N):

                    for j in range(i, N - 1):
                        copylst = lst[:]
                        a_lst = []
                        a_lst.append(copylst.pop(i))
                        a_lst.append(copylst.pop(j))
                        if not a_lst in B_group:
                            A_group.append(a_lst)
                            B_group.append(copylst)
            elif i == 3:

                for i in range(N):

                    for j in range(i, N - 1):
                        for k in range(j, N - 2):
                            copylst = lst[:]
                            a_lst = []
                            a_lst.append(copylst.pop(i))
                            a_lst.append(copylst.pop(j))
                            a_lst.append(copylst.pop(k))
                            if not a_lst in B_group:
                                A_group.append(a_lst)
                                B_group.append(copylst)
            elif i == 4:
                for i in range(N):

                    for j in range(i, N - 1):
                        for k in range(j, N - 2):
                            for u in range(k, N - 3):
                                copylst = lst[:]
                                a_lst = []
                                a_lst.append(copylst.pop(i))
                                a_lst.append(copylst.pop(j))
                                a_lst.append(copylst.pop(k))
                                a_lst.append(copylst.pop(u))
                                if not a_lst in B_group:
                                    A_group.append(a_lst)
                                    B_group.append(copylst)


            B = len(B_group)
            final_B = []
            for i in range(B):
                result_B = 0
                copy_B = B_group[i][:]
                for j in range(len(B_group[i])):
                    if not copy_B:
                        for u in range(B):
                            result_B += people[B_group[i][u]]
                            break

                    for k in range(j + 1, len(B_group[i])):
                        if arr[B_group[i][j]][B_group[i][k]] == 0:
                            continue
                        if arr[B_group[i][j]][B_group[i][k]] == 1:
                            try:
                                index1 = copy_B.index(B_group[i][j])
                                index2 = copy_B.index(B_group[i][k])
                                copy_B.pop(index2)
                                copy_B.pop(index1)

                            except:
                                try:
                                    index2 = copy_B.index(B_group[i][k])
                                    copy_B.pop(index2)
                                except:
                                    continue

                        if not copy_B:
                            break

                final_B.append(result_B)


            A = len(A_group)

            final_A = []
            for i in range(A):
                result_A = 0
                copy_A = A_group[:]
                if len(A_group[i]) != 1:
                    for j in range(len(A_group[i])):
                        if not copy_A:
                            for u in range(A):
                                result_A += people[A_group[i][u]]
                                break

                        for k in range(j + 1, len(A_group[i])):
                            if arr[A_group[i][j]][A_group[i][k]] == 0:
                                continue
                            if arr[A_group[i][j]][A_group[i][k]] == 1:
                                try:
                                    index1 = copy_A.index(A_group[i][j])
                                    index2 = copy_B.index(A_group[i][k])
                                    copy_A.pop(index2)
                                    copy_A.pop(index1)

                                except:
                                    try:
                                        index2 = copy_B.index(A_group[i][k])
                                        copy_A.pop(index2)
                                    except:
                                        continue

                            if not copy_A:
                                break

                    final_A.append(result_A)
                else:
                    result_A += people[A_group[i][0]]

                    final_A.append(result_A)



            for i in range(len(final_B)):
                if abs(final_B[i]-final_A[i]) == 0:
                    return 0
                else:
                    if result > abs(final_B[i] - final_A[i]):
                        result = abs(final_B[i] - final_A[i])


        return result

    result = area()
    print(result)

'''
5
0 1 0 1 0
1 0 1 1 1
0 1 0 0 0
1 1 0 0 1
0 1 0 1 0
10 10 3 10 7
6
0 1 0 0 0 1
1 0 0 1 1 1
0 0 0 1 0 0
0 1 1 0 0 0
0 1 0 0 0 0
1 1 0 0 0 0
13 18 8 5 18 5
6
0 1 1 1 1 0
1 0 0 0 1 0
1 0 0 0 1 0
1 0 0 0 0 1
1 1 1 0 0 1
0 0 0 1 1 0
17 11 7 15 4 11
7
0 1 0 0 0 0 1
1 0 0 0 0 1 1
0 0 0 0 0 1 1
0 0 0 0 1 0 0
0 0 0 1 0 1 1
0 1 1 0 1 0 0
1 1 1 0 1 0 0
15 18 14 9 7 7 12
7
0 1 0 1 0 1 0
1 0 0 1 0 0 0
0 0 0 0 0 1 0
1 1 0 0 1 0 0
0 0 0 1 0 1 1
1 0 1 0 1 0 0
0 0 0 0 1 0 0
20 20 3 12 6 16 13
7
0 1 0 0 1 0 0
1 0 0 0 1 1 1
0 0 0 1 0 1 0
0 0 1 0 1 0 0
1 1 0 1 0 0 0
0 1 1 0 0 0 0
0 1 0 0 0 0 0
9 16 16 12 19 18 4
7
0 0 0 0 1 1 0
0 0 0 0 0 1 1
0 0 0 1 0 1 1
0 0 1 0 1 1 0
1 0 0 1 0 0 1
1 1 1 1 0 0 0
0 1 1 0 1 0 0
13 15 3 14 9 19 3
8
0 0 0 0 0 0 0 1
0 0 0 1 0 0 1 0
0 0 0 1 1 0 1 0
0 1 1 0 0 0 0 0
0 0 1 0 0 1 0 0
0 0 0 0 1 0 1 0
0 1 1 0 0 1 0 1
1 0 0 0 0 0 1 0
5 6 20 9 3 17 17 14
8
0 0 0 1 0 1 1 0
0 0 0 0 0 0 1 0
0 0 0 0 0 0 1 0
1 0 0 0 1 0 0 0
0 0 0 1 0 0 0 1
1 0 0 0 0 0 0 0
1 1 1 0 0 0 0 1
0 0 0 0 1 0 1 0
12 4 6 16 3 15 13 7

'''

