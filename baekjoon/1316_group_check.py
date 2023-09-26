# N = int(input())
# arr = [list(input()) for _ in range(N)]
# cnt = 0
# for i in arr:
#     j = 0
#     dict = {}
#     lst = []
#     while True:
#
#         if lst: # 리스트에 있으면 그 단어는 continue(for문안에 while이므로 break)
#             break
#         if j == len(i):
#             cnt += 1
#             break
#         if i[j] not in dict and i[j] not in lst: # dict에 없다면 새로 추가하면서 그 인덱스 추가
#             dict[i[j]] = j
#             j += 1
#             continue
#         elif i[j] in dict and i[j] not in lst: # dict에 있다면 인덱스 비교하며 그 단어의 키값의 숫자보다 인덱스가 1크다면
#             if dict[i[j]] == j-1:
#                 dict[i[j]] = j #키값의 숫자 업데이트
#                 j += 1
#             else:  # 만약에 있는데 1차이가 아니라면 삭제하고 리스트에 추가
#                 dict.pop(i[j])
#                 lst.append(i[j])
#                 j += 1
# print((cnt))


from collections import deque
T = int(input())
cnt = 0 # 몇개인지 세는거
for tc in range(T):
    # flag = 0 # 나갈지 말지 정하는거
    arr = list(input())
    arr = deque(arr)
    check = [] # 왼쪽부터 뽑아서 여기다가 넣음

    while arr: # arr 전부 뽑을거임
        now = arr.popleft()
        if now in check: #만약 뽑은게 체크리스트에 있으면
            if now != before: #있으면서 before(바로전에 뽑은거)랑 다르면
                # flag = 1 # 넌 나가라
                break # 안돌릴거임
            # else: #없으면
            #     continue # 계속 돌려
        else: # 체크리스트에 없으면
            check.append(now) #체크리스트에 넣어
        before = now # 바로전거 갱신해주는거
        if arr == deque([]): # 나가지도 않고 다 뽑았으면
            cnt += 1
            # break# 갯수 세줌
print(cnt)

# while 을 쓰려면 탈출 조건이 존재 해야함

# pop(0)
# 없으면 리스트 추가
# 바로 전꺼 리스트에 있는데 바로전꺼랑 다르면 break
# break되었으면 다음단어로 ㄱㄱ
# 근데 break없이 while다 돌았으면