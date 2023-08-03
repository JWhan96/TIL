T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charge_point = list(map(int, input().split()))

    def elecbus(charge_point):

        charge_count = 0
        bus_location = 0

        while True:
            # print(bus_location)
            if bus_location == 0:
                for i in range(0, M - 1):
                    if charge_point[i] + K < charge_point[i + 1]:
                        return 0

            if bus_location >= N:
                break
            elif (bus_location in charge_point) or (bus_location == 0):
                if bus_location in charge_point:
                    charge_count += 1
                bus_location += K
                # print(f'ㅇ{bus_location}')

            elif bus_location not in charge_point:
                bus_location -= 1

        return charge_count
    result = elecbus(charge_point)
    print(f'#{tc} {result}')

####def쓰기전
    # charge_count = 0
    # bus_location = 0
    #
    # while True:
    #     # print(bus_location)
    #     for i in range(0, M - 1):
    #         if charge_point[i] + K < charge_point[i + 1]:
    #             charge_count = 0
    #             bus_location = N
    #             break
    #
    #     if bus_location >= N:
    #         break
    #     if (bus_location in charge_point) or (bus_location == 0):
    #         if bus_location in charge_point:
    #             charge_count += 1
    #         bus_location += K
    #         # print(f'ㅇ{bus_location}')
    #
    #     elif bus_location not in charge_point:
    #         bus_location -= 1
    #         continue
    # print(f'#{tc} {charge_count}')




   #####강사님 풀이1

    # ch = [0] * (N + 1)
    # for i in charge_point:
    #     ch[i] += 1
    # current = 0 #현재 위치
    # count = 0 #충전 횟수
    #
    # while current < N:
    #     # 갈수 있는 최대 거리 계산
    #     if ch[current + K]:
    #         current += K
    #         count += 1
    #     # 충전소 찾기(뒤로 한칸씩 가면서
    #     else:
    #         for j in range(1, K):
    #
    #             # 충전소를 찾으면 충전, count 증가
    #             if ch[current + K - j]:
    #                 current += current + K - j
    #                 count += 1
    #                 break
    #             # 충전소가 없으면, count = 0, 반복종료
    #         else:
    #             count = 0
    #             break
    # # 최대 거리가 도착점보다 멀거나 같으면, 반복종료
    #     if current + K >= N:
    #         current = N
    # print(f'#{tc} {count}')


####강사님 풀이 2
    # curr, cnt = 0, 0
    # while curr != N:
    #     #curr+K :한번 충전으로 갈 수 있는 거리, N: 종점까지 거리
    #     if N <= curr + K:
    #         curr = N
    #         break
    #     #충전소 뒤에서 부터 순회
    #     for i in range(len(charge_point)-1, -1, -1):
    #         #리스트 arr의 값이 curr+K 이내에 있다면
    #         if charge_point[i] <= curr + K:
    #             cnt += 1 # 충전횟수 증가
    #             curr = charge_point[i] #현재 위치를 충전소 위치로 변경
    #             charge_point = charge_point[i+1:] # 해당 충전소 이후의 정류장만 남기기
    #         #충전소를 찾지 못하였다면
    #         if i == 0:
    #             cnt = 0
    #             curr = N
    # print(f'#{tc} {cnt}')









    # charge_count = 0
    # bus_location = 0
    #
    # while True:
    #     # print(bus_location)
    #     for i in range(0, M - 1):
    #         if charge_point[i]+K < charge_point[i+1]:
    #             charge_count = 0
    #             bus_location = N
    #             break
    #
    #     if bus_location >= N:
    #         break
    #     if (bus_location in charge_point) or (bus_location == 0):
    #         if bus_location in charge_point:
    #             charge_count += 1
    #         bus_location += K
    #         # print(f'ㅇ{bus_location}')
    #
    #     elif bus_location not in charge_point:
    #         bus_location -= 1
    #         continue
    #
    # print(f'#{tc} {charge_count}')

