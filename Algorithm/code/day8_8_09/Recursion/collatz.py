N = int(input())
lst = []
count = 0
def coll(n):
    global count
    d= 1
    if n == 1:
        return count
    elif n%2 == 1:
        coll(n*3+1)
        count += 1
    elif n%2 == 0:
        coll(n//2)
        count += 1
    return count

print(coll(N))
# ##########
# N = int(input())
# count = 0
# def coll(n, count):
#     d= 1
#     if n == 1:
#         return count
#     elif n%2 == 1:
#         coll(n*3+1, count+1)
#
#     elif n%2 == 0:
#         coll(n//2, count+1)
#     else:
#         return count
#
# print(coll(N, 0))