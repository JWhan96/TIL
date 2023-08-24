import sys
def check_inclusion():
    for i in range(len(arr) - 1):
        current_element = arr[i]
        cur = len(current_element)
        next_element = arr[i + 1][0:cur]

        if current_element in next_element:
                return 'NO'

    return'YES'

T = int(input())
for tc in range(1, T+1):
    N = int(sys.stdin.readline().rstrip())
    ar = list(sys.stdin.readline().rstrip() for _ in range(N))
    arr = sorted(ar)
    result = check_inclusion()
    print(result)

# ['911', '91125426', '97625999']
# ['113', '12340', '123440', '12345', '98346']

