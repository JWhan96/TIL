# N = int(input())
#
# def binary(N):
#
#     if N == 0:
#
#         return
#     # if N == 1:
#     #     print(1)
#     #     return
#
#     binary(N // 2)
#     print(N % 2)
#     if N%2 == 0:
#         print(0)
#         return
#
#
# binary(N)

########
# def func(n):
#     if n == 0:
#         return '0'
#     elif n == 1:
#         return '1'
#     else:
#         return func(n//2) + str(n%2)
#
# print(func(N))
result = ''
def binary(n):
    d=1
    global result
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:

        result = binary(n//2) + str(n%2)

    return result
print(binary(5))