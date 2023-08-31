import itertools

def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

N = int(input())
fib_sequence = list(itertools.islice(fibonacci(), N))

print(fib_sequence)
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]