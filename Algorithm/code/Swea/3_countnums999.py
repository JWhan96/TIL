###회문 문제 활용해서 풀어보기
#$#####




##메서드 가능 방법
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    cnt_list = []
    #str1의 문자를 하나씩 str2와 비교
    for i in str1:
        cnt_list.append(str2.count(i))
    result = max(cnt_list)
    print(f'#{tc} {result}')




##방법 2
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    result = 0
    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                cnt += 1
        if result < cnt:
            result = cnt
    print(f'#{tc} {result}')