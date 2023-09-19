N, M = map(int, input().split())
path = [0] * 10 # 주사위를 던져 나온값을 저장하는 path리스트
def printpath(level):
    print(' '.join(map(str, path[:level]))) #주사위 값을 문자열로 변환하여 공백을 넣어 출력

def roll1(level): # M = 1일 때 N번 주사위 던져서 나올 수 있는 모든 경우
    if level == N: #주사위를 N번 던졌다면 결과 출력
        printpath(level)
        return
    for i in range(1, 7):
        path[level] = i #1. 현재 레벨의 주사위 값을 i로 설정
        roll1(level + 1) #2. 다음레벨로 재귀 호출
        path[level] = 0 #3. 백트래킹: 현재 레벨의 주사위 값을 초기화

def roll2(level): # M = 2일때
    if level == N: #주사위를 N번 던졌다면 결과 출력
        printpath(level)
        return
    for i in range(1, 7):
        if level > 0 and i < path[level - 1]: # 중복 제거조건
            continue
        path[level] = i #1. 현재 레벨의 주사위 값을 i로 설정
        roll2(level + 1) #2. 다음레벨로 재귀 호출
        path[level] = 0 #3. 백트래킹: 현재 레벨의 주사위 값을 초기화

DAT = [0] * 10

def roll3(level): # M = 3일때
    if level == N: #주사위를 N번 던졌다면 결과 출력
        printpath(level)
        return
    for i in range(1, 7):
        if DAT[i] == 1: #사용한 눈금은 스킵
            continue
        DAT[i] = 1 #현재 레벨에서 i눈금 사용 체크
        path[level] = i  # 1. 현재 레벨의 주사위 값을 i로 설정
        roll1(level + 1)  # 2. 다음레벨로 재귀 호출
        path[level] = 0  # 3. 백트래킹: 현재 레벨의 주사위 값을 초기화
        DAT[i] = 0 #백트래킹: i눈금 사용 체크 초기화

if M == 1:
    roll1(0)
elif M == 2:
    roll2(0)
elif M == 3:
    roll3(0)