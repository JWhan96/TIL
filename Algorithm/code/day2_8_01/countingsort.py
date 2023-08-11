def Counting_Sort(A, B, k):
    pass
a = [0, 4, 1, 3, 1, 2, 4, 1]
b = []
c = []

c = [0] * (8)
for i in range(0, len(a)):
    c[a[i]] += 1
    # print(c)
for i in range(1, len(c)):
    c[i] += c[i-1]
    # print(c)
for i in range((len(b)-1), -1, -1):
    c[a[i]] -= 1
    b[c[a[i]]] = a[i]
# print(b)
    print(c)
