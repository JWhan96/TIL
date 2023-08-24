T = int(input())
for tc in range(1, T+1):
    arr = input()
    S = []
    D = []
    H = []
    C = []
    for i in range(1, 13+1):
        S.append(i)
        D.append(i)
        H.append(i)
        C.append(i)


    for i in range(len(arr)-2):
        try:
            if arr[i] == 'S':
                s = S.index(int(arr[i+1:i+2+1]))
                S.pop(s)
            if arr[i] == 'D':
                d = D.index(int(arr[i+1:i+2+1]))
                D.pop(d)
            if arr[i] == 'H':
                h = H.index(int(arr[i+1:i+2+1]))
                H.pop(h)
            if arr[i] == 'C':
                c = C.index(int(arr[i+1:i+2+1]))
                C.pop(c)
        except:
            result = 'ERROR'
            print(f'#{tc} {result}')
            break

    else:
        print(f'#{tc} {len(S)} {len(D)} {len(H)} {len(C)}')
