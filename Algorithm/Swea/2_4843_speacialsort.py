T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N-1):
        chooseIdx = i
        for j in range(i+1, N):
            if i % 2 == 0:
                if arr[chooseIdx] < arr[j]:
                    chooseIdx = j
            else:
                if arr[chooseIdx] > arr[j]:
                    chooseIdx = j

        arr[i], arr[chooseIdx] = arr[chooseIdx], arr[i]
    print(f'#{tc}', *arr[:10])


### 강사님 코드
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     numbers = list(map(int, input().split()))
#     result = []
#
#     while len(numbers)>0:
#         max_value = max(numbers)
#         numbers.remove(max_value)
#         result.append(max_value)
#
#         min_value = min(numbers)
#         numbers.remove(min_value)
#         result.append(min_value)
#
#     print(f'#{tc}', *result[:10])