# N = int(input())
# arr = []
# for i in range(1, N+1):
#     arr.append(str(i))
# # print(arr)
#
# for i in range(len(arr)):
#     clab = 0
#     if '3' in arr[i] or '6' in arr[i] or '9' in arr[i]:
#         clab += arr[i].count('3')
#         clab += arr[i].count('6')
#         clab += arr[i].count('9')
#         arr [i] = clab*'-'
#     else:
#         arr[i] = arr[i]
# print(*arr)

def Bbit_print(i):
    output = ''
    for j in range(7, -1, -1):
        output += '1' if i & (1 << j) else '0'
    print(output)
a = 0x86
key = 0xAA

print('a ==> ', end='')
Bbit_print(a)

print('a^=key  ==> ', end='')
a ^= key
Bbit_print(a)

print('a^=key  ==> ', end='')
a ^= key
Bbit_print(a)

#
# for i in range(-5, 6):
#     print('%3d = ' % i, end='')
#     Bbit_print(i)
# a = 0x10
# x = 0x01020304
# print('%d = ' %a, end='')
# Bbit_print(a)
# print()
# print('0%X = ' %x, end = '')
# for i in range(0, 4):
#     Bbit_print((x >> i*8) & 0xff)

# def ce(n): #change endian
#     p = []
#     for i in range(0, 4):
#         p.append((n >> (24 - i*8)) & 0xff)
#     return p
# x = 0x01020304
# p = []
# for i in range(0, 4):
#     p.append((x >> (i*8)) & 0xff)
#
# print('x = %d%d%d%d' % (p[0], p[1], p[2], p[3]))
# p = ce(x)
# print('x = %d%d%d%d' % (p[0], p[1], p[2], p[3]))


