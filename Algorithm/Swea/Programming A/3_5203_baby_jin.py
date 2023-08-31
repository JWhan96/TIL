def check_win(cards):
    cnt = [0] * 10
    for num in cards:
        cnt[num] += 1 # 카드 숫자세기
    #triplet 확인
    if 3 in cnt:
        return True
    # run 확인
    for i in range(8):
        if 0 not in cnt[i : i+3]:
            return True
    return False

T = int(input())
for tc in range(1, T+1):
    all_cards = list(map(int, input().split()))
    p1 = []
    p2 = []
    winner = 0
    for i in range(6):
        p1.append(all_cards[i*2]) #짝수 인덱스 카드
        if len(p1) >2 and check_win(p1):
            winner = 1
            break
        p2.append(all_cards[i*2+1])
        if len(p1) > 2 and check_win(p2):
            winner = 2
            break
    print(f'#{tc} {winner}')