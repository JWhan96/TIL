S = input()
s = S.upper()
arr = list(s)
arr.sort() #['I', 'I', 'I', 'I', 'M', 'P', 'S', 'S', 'S', 'S']
# 65~90
lst1 = []
for i in range(65, 91):
    lst1.append(chr(i))

lst2 = []
q = ''
max_v = 0
for i in range(len(lst1)):
    lst2.append(arr.count(lst1[i]))
for i in range(len(lst2)):
    if lst2[i] > max_v:
        max_v = lst2[i]
        q = lst1[i]
max_cnt = lst2.count(max_v)
if max_cnt == 1:
    print(q)
else:
    print('?')