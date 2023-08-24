## Start
### 목차
- [SW 문제 해결]
- [복잡도 분석]
- [표준 입출력 방법]
- [비트 연산]
- [진수]
- [실수]





### 비트 연산



#### 비트 연산 예제 1
```py
def Bbit_print(i):
    output = ''
    for j in range(7, -1, -1):
        output += '1' if i & (1 << j) else '0'
    print(output)

for i in range(-5, 6):
    print('%3d = ' % i, end='')
    Bbit_print(i)
```
```
출력
-5 = 11111011
-4 = 11111100
-3 = 11111101
-2 = 11111110
-1 = 11111111
0 = 00000000
1 = 00000001
2 = 00000010
3 = 00000011
4 = 00000100
5 = 00000101
```

#### 비트 연산 예제 2
```py
def Bbit_print(i):
    output = ''
    for j in range(7, -1, -1):
        output += '1' if i & (1 << j) else '0'
    print(output, end = ' ')
a = 0x10
x = 0x01020304
print('%d = ' %a, end='') # 16 =
Bbit_print(a)  #00010000
print()
print('0%X = ' %x, end = '')  #01020304 =
for i in range(0, 4):
    Bbit_print((x >> i*8) & 0xff) # 00000100 00000011 00000010 00000001
```
```
출력
16 = 00010000
01020304 = 00000100 00000011 00000010 00000001
```
#### 비트 연산 예제 3
```py
def ce(n): #change endian
    p = []
    for i in range(0, 4):
        p.append((n >> (24 - i*8)) & 0xff)
    return p
x = 0x01020304
p = []
for i in range(0, 4):
    p.append((x >> (i*8)) & 0xff)

print('x = %d%d%d%d' % (p[0], p[1], p[2], p[3]))
p = ce(x)
print('x = %d%d%d%d' % (p[0], p[1], p[2], p[3]))
```
```
출력
x = 4321
x = 1234
```
#### 비트 연산 예제 4(??????????????)
```py
def ce1(n):
    return (n << 24 & 0xff000000) | (n << 8 & 0xff0000) | (n >> 8 & 0xff00) | (n >> 24 & 0xff)
```
#### 비트 연산 예제 5
```py
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
```
```
출력
a ==> 10000110
a^=key  ==> 00101100
a^=key  ==> 10000110
```