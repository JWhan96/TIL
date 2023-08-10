T = int(input())
for tc in range(1, T+1):
    string = list(input())
    stack = []
    for char in string:
        # 만약 반복 문자라면 (스택에 문자가 있고, 현재 문자가 스택의 마지막 문자와 같다면
        if stack and char == stack[-1]:
            stack.pop() # 반복문자 제거
        else:
            stack.append(char)
    print(f'#{tc} {len(stack)}')
            