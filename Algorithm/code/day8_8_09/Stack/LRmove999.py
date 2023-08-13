'''
R
R
R
L

9 7 3 5 1
'''

# arr = [3, 5, 1, 9, 7]
# arr_T = []
# for i in range(4):
#     D = input()
#     if D == R:
#         for j in range(5):
#             if j+1 > 5:
#                 arr[j]
#             arr_T[j+1] = arr[j]
#
arr = ['3', '5', '1', '9', '7']

T= [(input()) for _ in range(4)]

def Right(lst):
    #리스트 뒤쪽에 앞의 4개의 원소 추가
    for i in range(4):
        lst.append(lst[i])
    #리스트 앞쪽의 4개의 요소 제거
    for _ in range(4):
        lst.pop(0)
def Left(lst):
    lst.append(lst[0]) #리스트 맨 앞의 요소를 맨 뒤에 추가
    lst.pop(0) #리스트 맨 앞의 요소 제거

for i in range(4):
    if T[i] == 'R':
        Right(arr)
    if T[i] == 'L':
        Left(arr)

print(*arr)