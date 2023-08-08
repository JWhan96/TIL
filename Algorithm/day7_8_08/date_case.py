# 가능한 날짜 찾기(날짜 경우의 수)
# 세부사항
# 1. 10, 11, 12월은 두 자릿수로 표현하고 1~9월은 한 자릿수로 표현(07월이 아닌 7월)
# 2. 년도는 네자리로 표현
# 3. 날짜는 모든 달이 1~31일이라고 가정, 1~9일은 한자릿수로(04일이 아닌 4)
# 4. 년도 부분에 찢어질 수도 있지만 년도가 찢어지는 것은 무시
# (예를 들어 xxxx.12.3인 경우 년도를 무시하므로 가능한 날짜는 1개)
# 5. X의 개수는 최대 8개까지 가능 ex)xxxx.xx.xx

# [예시]
# 2032.X.20 : 1~9까지 올 수 있으므로 정답은 9
# 2011.9.XX : 10~31까지 올 수 있으므로 정답은 22
'''
2025.X.1X

90
'''
##내방법
# arr = list(input().split('.'))
# year_list = arr[0]
# month_list = arr[1]
# day_list = arr[2]
# count_month = 1
# count_day = 1
#
#
# if len(month_list) == 1 and month_list == 'X':
#     count_month *= 9
# elif len(month_list) == 2:
#     if month_list == 'XX':
#         count_month *= 3
#     elif month_list[1] == 'X':
#         count_month *= 3
#
# if len(day_list) == 1 and day_list == 'X':
#     count_day *= 9
# elif len(day_list) == 2:
#     if day_list == 'XX':
#         count_day *= 22
#     elif day_list[1] == 'X':
#         count_day *= 10
#     elif day_list[0] == 'X' and 2 <= int(day_list[1]) <= 9:
#         count_day *= 2
#     elif day_list[0] == 'X' and 0 <= int(day_list[1]) <= 1:
#         count_day *= 3
# print(f'{count_month * count_day}')

###강사님 방법(별 차이없음)
def year_cnt(year):
    # 전부X
    if year == 'XXXX':
        return 1
    #4자리
    #1자리
    if year[0] == 'X':
        a = 9
    if year[1] == 'X':
        b = 10
    if year[2] == 'X':
        c = 10
    if year[3] == 'X':
        d = 10
    return a*b*c*d

def month_cnt(month):
    #1자리
    if len(month) == 1:
        if month == 'X':
            return 9
    if len(month) == 2:
        if month[1] == 'X':
            return 3
    return 1

def day_cnt(day):
    # 1자리
    if len(day) == 1:
        if day == 'X':
            return 9
    if len(day) == 2:
        if day == 'XX':
            return 22
        if day[0] == 'X':
            # if day[1] == '0' or day[1] == '1':
            #     return 3
            return 2
        if day[1] == 'X':
            if day[0] != '3':
                return 3
            return 2
    return 1

print(month_cnt(str(input())))
print(day_cnt(str(input())))