import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
lst = []
arr = [(int(input())) for _ in range(N)]
stack = [1]
i = 2
j = 0
result = ['+']
cnt = 0
while True:
    if cnt == N:
        break

    if not stack:
        stack.append(i)
        i += 1
        result.append('+')
    if arr[j] < stack[-1]:
        break
    if arr[j] != stack[-1] and i <= N:
        stack.append(i)
        i += 1
        result.append('+')
    elif arr[j] == stack[-1]:
        lst.append(stack.pop())
        j += 1
        result.append('-')
        cnt += 1


if lst == arr:
    for i in result:
        print(i)
else:
    print('NO')