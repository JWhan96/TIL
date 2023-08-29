T = int(input())
for tc in range(1, T+1):
    n, r = map(int, input().split())
    foods = list(map(int, input().split()))
    arr = foods * 2 #원형 테이블 고려
    DAT = [0] *201 #각 음식의 개수를 저장할 리스트
    # 시작 끝 인덱스 초기화

    start = 0
    end = 2* r
    flag = 0 # 서빙에 성공했는지 판단하는 변수
    # 초기 구간에서 음식의 개수를 세고 , 3개 이상 중복되는지 확인
    for k in range(start, end):
        DAT[arr[k]] += 1
        if DAT[arr[k]] >2:
            flag = 1
            break
    # 슬라이딩 윈도우 기법
    while end < 2 *n and flag == 0: #end포인터가 리스트의 끝에 도달하거나 flag가 1이되면 종료
        DAT[arr[end]] +=1
        if DAT[arr[end]] >2:
            flag = 1
            break
        #스타트 포인터가 가리키는 요소의 빈도수 1 감수
        DAT[arr[start]] -= 1
        start += 1 #스타트 엔드 1씩 증가시켜 다음요소로 이동
        end += 1
    if flag == 1:
        print(f'#{tc} NO')
    else:
        print(f'#{tc} YES')