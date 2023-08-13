'''
입력
AB100CDEF112F4G5
출력
AB#117
CDEF#112
...
'''
word = input()
result = ''
index = 0  # 인덱스 초기화

while index < len(word):
    temp = ''
    d= 1
    if not word[index].isdigit():
        while index < len(word) and not word[index].isdigit():
            temp += word[index]
            index += 1
        result += temp + '#'
    elif word[index].isdigit():
        while index < len(word) and word[index].isdigit():
            temp += word[index]
            index += 1
          # 빈 문자열이 아닐 때에만 처리
        result += str(int(temp) + 17)
        print(result)
        result = ''

#####태규 코드
# def split_combined_strings(st):
#
#     result = []
#     current_item = ""
#     is_number = False
#
#     for char in st:
#         if char.isdigit():
#             if is_number == False:
#                 current_item += '#'
#                 result.append(current_item)
#                 current_item = ""
#             current_item += char
#             is_number = True
#         else:
#             if is_number:
#                 current_result = int(current_item)
#                 result.append(current_result + 17)
#                 current_item = ""
#                 is_number = False
#         if not char.isdigit():
#             current_item += char
#
#
#
#
#     return result
#
# st = input()
# st = st + 'a'
# split_result = split_combined_strings(st)
# result_list = []
#
# for i in range(0, len(split_result) - 1, 2):
#     result = split_result[i] + str(split_result[i+1])
#     result_list.append(result)
#
# for i in result_list:
#     print(i)



