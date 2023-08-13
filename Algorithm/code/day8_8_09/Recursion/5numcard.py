# 다섯종류 카드 입력('0' ~ '9')
# 카드는 충분히 존재
# 5종류의 숫자카드에서 4장 뽑기
# 뽑을때마다 전에 뽑았던 카드번호와 간격이 3이하로 차이나는 중복순열이 몇가지 인지 출력
# 재귀호출 사용

'''
카드종류 1/2/3/4/5
1111: OK
1112: OK
1113: OK
1114: OK
1115: [NO]
1121: OK
...
no count 숫자: 1251, 5123...등등
'''
# 총 497가지
# 힌트
# path[level-1]와 path[level]의 절대값이 3차이 나는지 확인


# def combinations_3(array, r):
#     for i in range(len(array)):
#         if r == 1:
#             yield [array[i]]
#         else:
#             ## array[i+1: ] -> array[i: ] 변경
#             for next in combinations_3(array[i:], r-1):
#                 if array[i] != array[i-1]:
#                     yield [array[i]] + next
#
# for i in combinations_3([1,2,3,4,5],2):
#     print(i, end=" ")

card = list(input())
path = [0] * 4
cnt = 0

def card_cnt(level):
    global cnt
    d=1
    # 4장의 카드를 뽑았으면 경우의 수 증가
    if level == 4:
        cnt += 1
        return  # 재귀호출종료
    for i in range(5):  # 5개의 카드중 하나 선택
        path[level] = card[i]  # 현재 레벨 경로에 -> 선택한 카드를 저장
        # 연속된 카드간의 차이가 4이상이면 -> 다음 카드 선택 -> 백트래킹
        if int(path[level]) - int(path[level-1]) >= 4:
            continue
        if int(path[level-1]) - int(path[level]) >= 4:
            continue
        # 다음 레벨로 재귀 호출
        card_cnt(level+1)
card_cnt(0)
print(cnt)
































#
# # 뽑은 카드가 유효한지 확인
# def isvalid(result):
#     # 1115
#     for i in range(3):
#         if abs(int(result[i]) - int(result[i+1])) > 3:
#             return False
#     return True
#
# # 중복 순열 만들기
# def comb(start):
#     global cnt
#     if len(result) == 4:
#         if isvalid(result):
#             cnt += 1
#         return
#
#     for i in range(start, len(N)):
#         result.append(N[i])
#         comb(0)
#         result.pop()
#
# result = []
# cnt = 0
# comb(0)
# print(cnt)

