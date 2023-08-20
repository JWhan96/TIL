stack = [0] * 100
top = -1
susik = '6528-*2/+'
for x in susik:
    if x not in '+-/*':  # 피연산자라면
        top += 1
        stack[top] = int(x)
    else:
        op2 = stack[top]  # pop()
        top -= 1
        op1 = stack[top]  # pop()
        top -= 1

        if x == '+':
            top += 1
            stack[top] = op1 + op2
        elif x == '-':
            top += 1
            stack[top] = op1 - op2

        elif x == '/':
            top += 1
            stack[
                top] = op1 // op2  # //로 하는 이유는 나누어 떨어진다는 가정하에 int로 받기 위해서 나누어 떨어진다는 가정이 없다면 //로 받은 이후 소수점을 버리거나 int화 해야한다(/연산결과: float)

        elif x == '*':
            top += 1
            stack[top] = op1 * op2

print(stack[top])  # -9