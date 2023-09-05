# print(ord('a'))
# print(ord('z'))
arr = (input())
lst = []
for i in range(97, 123):
    lst.append(chr(i))
for i in range(len(lst)):
    print(arr.find(lst[i]), end = ' ')

