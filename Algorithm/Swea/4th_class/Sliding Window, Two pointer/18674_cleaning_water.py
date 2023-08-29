
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
# 투포인터 초기화
left = 0
right = n-1
#변수 초기화
minimum = 2e9 +1
ansleft = 0
ansright = 0
while left < right:
    sum = arr[left] + arr[right] #합구하기
    # 합이 0이면 두수를 출력하고 프로그램 종료
    if sum == 0:
        print(arr[left], arr[right])
        exit() #break와 exit()차이 -> exit은 프로그램 자체를 완전 종료
    # 절대 값 이요 최소차이 찾기
    if minimum > abs(sum):
        minimum = abs(sum)
        ansleft = left
        ansright = right
    #합이 0보다 크면 right줄이고 합이 0보다 작으면 left늘리기
    if sum > 0:
        right -= 1
    else:
        left += 1

print(arr[ansleft], arr[ansright])

