a = [1, 2, 3, 4]
N = 4

# for i in range(1, (1<<N)-1): # 2의 N승번 반복(1이 왼쪽으로 N번만큼 이동)
#     subset1 = []
#     subset2 = []
#     for j in range(N):
    
#         if i & (1<<j): #j번 비트가 0이 아니면
#             subset1.append(a[j])
#         else:
#             subset2.append(a[j])
#     print(subset1, subset2)

## 나누었을때 중복된 집합들을 없애기 위해
# (1<<N)//2 == 1<<(N-1)까지만
for i in range(1, (1<<N)//2): # 2의 N승번 반복(1이 왼쪽으로 N번만큼 이동)
    subset1 = []
    subset2 = []
    for j in range(N):
    
        if i & (1<<j): #j번 비트가 0이 아니면
            subset1.append(a[j])
        else:
            subset2.append(a[j])
    
    print(subset1, subset2)

