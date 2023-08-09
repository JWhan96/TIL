# N = int(input())
# lst = []
# def coll(n):
#
#     if n == 1:
#         return len(lst)
#     elif n%2 == 1:
#         coll(n*3+1)
#         lst.append(1)
#     elif n%2 == 0:
#         coll(n//2)
#         lst.append(1)
#     return len(lst)
#
# print(coll(N))
# ##########
N = int(input())
count = 0
def coll(n, count):
    d= 1
    if n == 1:
        return count
    elif n%2 == 1:
        coll(n*3+1, count+1)

    elif n%2 == 0:
        coll(n//2, count+1)
    else:
        return count

print(coll(N, 0))