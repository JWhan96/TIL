# T=int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [(input()) for _ in range(N)]
#     # print(arr)
#     def call():
#         # result = 0
#         for i in range(0, N):
#             q = len(arr[i])
#             for j in range(i+1, N):
#                 if len(arr[i]) <= len(arr[j]):
#                     if arr[i] == arr[j][:q]:
#                         # result += 1
#                         return print('No')
#         return print('Yes')
#
#     call()
    ######
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]

    def call():
        for i in range(0, N):
            q = len(arr[i])
            for j in range(i+1, N):
                if len(arr[i]) < len(arr[j]):
                    if arr[i] == arr[j][:q]:
                        return print('No')
        return print('Yes')

    call()