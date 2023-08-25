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


#######강사님 dictionary 이용

T = int(input())
for tc in range(1, T+1):
    card = input()
    check = []
    card_dict = {'S': 13, 'D': 13, 'H': 13, 'C': 13}  #무늬 별로 남은 카드수를 딕셔너리로 관리
    # 카드정보는 3글자씩 나누어 Check리스트에 저장
    for i in range(0, len(card), 3):
        check.append(card[i: i+3])
    # 중복 카드체크 -> set이용 -> Error출력
    if len(check) != len(set(check)):
        print(f'#{tc} ERROR')
    else:
        # 마지막 카드 정보의 첫글자 인덱스는 len(card) -3
        for i in range(0, len(card)-2, 3):
            num = card_dict[card[i]] - 1 #해당 무늬 카드수 1개 차감
            card_dict[card[i]] = num #딕셔너리 value에 업데이트
        print(f'#{tc}', *card_dict.values()) #딕셔너리 value출력 -> 남은 카드수

