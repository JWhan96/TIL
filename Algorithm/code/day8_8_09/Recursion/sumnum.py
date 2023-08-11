N = int(input())
t= 0
def sum(n):
    global t
    if n//10 == 0:
        t += n
        return t
    elif n//10 >= 1:
        t += n % 10 + sum(n//10)
        return t

print(sum(N))

## 간단히
def func(n):
    if n//10 ==0:
        return n
    return func(n//10) + n % 10
print(func(N))