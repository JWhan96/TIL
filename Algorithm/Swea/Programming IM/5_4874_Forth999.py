T = int(input())

def eval_postfix(arr):
    stack = []
    # try:
    for exp in arr:
        if exp.isdigit():
            stack.append(int(exp))
        elif exp == '.':
            if len(stack) == 1:
                result = stack.pop()
            else:
                result = 'error'
        elif not exp.isdigit(): #후위 표기식에 공백이 있을 경우에 무시
            n2 = stack.pop()
            n1 = stack.pop()
            if exp == "+":
                res = n1 + n2
            elif exp == "-":
                res = n1 - n2
            elif exp == "*":
                res = n1 * n2
            elif exp == '/':
                res = n1 // n2
            stack.append(res)

    return result

for tc in range(1, T+1):
    arr = list((input().split()))

    try:
        print(f'#{tc} {eval_postfix(arr)}')

    except:
        print(f'#{tc}', 'error')

