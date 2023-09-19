N = int(input())
DAT = [0] * 10
cnt = 0
def func(row):
    global cnt
    # N-1번 행까지 모두 castle을 각 행에 두었다면
    if row == N:
        cnt += 1 #하나의 조합을 찾았으니 cnt +=1
        return
    for col in range(N): # 각 행에서는 N개의 열을 둘 수 있다.
        if DAT[col] == 1: # 가지치기: 이미 이열에 castle을 둔적이 있다면,
            continue
        DAT[col] = 1 #현재 행에서 column에 castle을 하나 둔다
        func(row + 1) #현재 선택을 기반으로 다음 행의 배치를 탐색
        DAT[col] = 0 #백트래킹: 현재 열에 castle을 둔것을 해제
func(0)
print(cnt)