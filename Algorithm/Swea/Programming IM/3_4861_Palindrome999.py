# def is_pa(string):
#     #문자열을 뒤집어서 원본 문자열과 비교
#     return string == string[::-1]

def find_p(N, M, arr):
    for i in range(N):
        #각 행에서 가능한 시작 위치, M길이의 회문을 찾기위해서 N-M의 위치까지만 시작점 고려
        for j in range(N - M +1):
            #가로회문 -> 시작점 j에서 길이 M만큼의 부분 문자열
            h = arr[i][j : j+M]

            #세로회문 -> 시작점 j에서 길이 M만큼의 부분 리스트
            #k행 i열의 문자를 가져오면 세로로 문자를 읽을 수 있다.
            v = [arr[k][i] for k in range(j, j+M)]

            #회문 인지 판별
            if h == h[::-1]:
                # print(f'h: {h}')
                return h
            if v == v[::-1]:
                # print(f'v: {v}')
                return v

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]
    # arr_T = [list(row) for row in zip(*arr)]
    result = find_p(N, M, arr) #함수호출 회문찾기
    print(result)
    print(f'#{tc}', ''.join(result))







    #
    #
    #
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
