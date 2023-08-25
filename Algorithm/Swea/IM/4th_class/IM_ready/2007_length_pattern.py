T = int(input())
for tc in range(1, T+1):
    sent = input()
    for i in range(1, 11):
        madi = sent[:i]
        for j in range(i, 30 - (30 % i), i):
            if sent[j:j+i] != madi:
                break
        else:
            ans = i
            break
    print(f'#{tc}', ans)


'''
1
KORKOR44KORKOR44KORKOR44KORKOR44
'''

