'''
입력
AB100CDEF112F4G5
출력
AB#117
CDEF#112
...
'''

arr = input()

# def prisoner(arr):
lst = []
k = 0
for i in range(1, len(arr)):
    # if (arr[i-1].isdisit()):
    if (not arr[i].isdisit()):
        lst.append(arr[k:i])
        k = i
print(lst)
