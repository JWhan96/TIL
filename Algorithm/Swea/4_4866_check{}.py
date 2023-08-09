T = int(input())
for tc in range(1, T+1):
    text = input()


    # def Check(arr):
    #
    #     cntsmall = []
    #
    #     for i in range(len(arr)):
    #         # if check[i] == '[':
    #         #
    #         # if check[i] == '{':
    #         # print(arr[i])
    #         if arr[i] == '(':
    #             cntsmall.append('(')
    #         if cntsmall + arr[i] == ')' and cntsmall[-1] == '(':
    #             cntsmall.pop()
    #
    #         if arr[i] == '{':
    #             cntsmall.append('{')
    #         if arr[i] == '}' and cntsmall and cntsmall[-1] == '{':
    #             cntsmall.pop()
    #
    #
    #     result = len(cntsmall)
    #     return result
    #
    # result = Check(arr)
    # if result == 0:
    #     print(1)
    # else :
    #     print(0)

##############
    stack = []
    for i in text:
        if i == '{' or i == '(':
            stack.append(i)
        elif stack and i == '}' and stack[-1] == '{':
            stack.pop()
        elif stack and i == ')' and stack[-1] == '(':
            stack.pop()
        elif i == '}' or i == ')':
            stack.append(i)
    if stack:
        result = 0
    if len(stack) == 0:
        result = 1

    print(result)