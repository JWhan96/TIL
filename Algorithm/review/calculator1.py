stack = [0] * 100
top = -1
icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1, ')': 0}
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1, ')': 0}
fx= '(6+5*(2-8)/2)'

susik = ''


for x in fx:
    if x not in '(+-*/)': # 피연산자
        susik += x
    elif x == ')':  #'('까지 pop()
        while stack[top] != '(':
            susik += stack[top]
            top  -= 1
        top -= 1 # '('버림.pop
    else: #연산자라면: '(+-*/)'
        if top == -1 or isp[stack[top]] < icp[x]: #하나도 채워지지 않았거나 스택의 맨 위 요소보다 토큰의 우선순위가 더 높다면
            top += 1
            stack[top] = x # append()
        elif isp[stack[top]] >= icp[x]: #토큰의 우선순위가 더 낮다면
            while top > -1 and isp[stack[top]] >= icp[x]:
                susik += stack[top] # 수식에 스택요소 더하기 , pop()
                top -= 1
            top += 1
            stack[top] = x # 새로운 토큰 스택에 추가

print(susik) # 6528-*2/+