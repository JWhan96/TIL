# T = int(input())
# for tc in range(1, T+1):
#     N = str(input())
#     M = str(input())
#     result = 0
#     if N in M:
#         result += 1
#     else:
#         result = 0
#     print(f'#{tc} {result}')

###다른 방법
T = int(input())
for tc in range(1, T+1):
    str1 = str(input())
    str2 = str(input())

    result = 0
    #두번째 문자열 안에서 첫번째 문자열을 찾는다.
    for i in range(len(str2) - len(str1) + 1):
        cnt = 0
        #첫 번째 문자열 모든 문자 검사
        for j in range(len(str1)):
            #첫 번째 문자열의 j번째와 두번째 문자열의 i+j번째 문자가 일치하는지 확인
            if str1[j] == str2[i+j]:
                cnt += 1
        # print(cnt)
        #카운트가 첫 번째 문자열의 길이와 같다면
        if cnt == len(str1):
            result = 1

    print(f'#{tc} {result}')