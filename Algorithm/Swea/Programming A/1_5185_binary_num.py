# 3 비트연산 이용 
def bbb(val):
    for i in range(4):
        if val&(8>>i):
            print('1',end='')
        else:
            print('0',end='')
            
T = int(input())
for tc in range(1,T+1):
    N, S = input().split()
    print(f'#{tc}',end=' ')
    for i in range(0, int(N)): #길이만큼
        ten=int(S[i],16) # 16진수를 10진수로 바꾸기
        bbb(ten)
    print()

