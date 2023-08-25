# 5개의 단어, 길이는 1이상 15이하
T = int(input())
for tc in range(1, T+1):
    arr = [list(input()) for _ in range(5)]
    s= [[0]* 15 for _ in range(15)]
    for i in range(len(arr)): #칠판에 있는 단어 줄 수
        for j in range(len(arr[i])): # 각 단어의 글자수만큼
            s[i][j] = arr[i][j]
    word = ''
    for i in range(N):
        for j in range(15):
            if s[j][i] != 0: #해당위치에 글자가 있다면
                word += s[j][i] # 문자열에 글자 추가
    print(f"#{tc} {word}")



lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
[1][2][3~9]
[1][2,3][4~9]
[1][2, 3, 4][5~9]