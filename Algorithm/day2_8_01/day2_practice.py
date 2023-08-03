# vscode keymap 설치 -> 적용
### 버블정렬: 인접한 두 요소를 비교하여 큰 값을 오른쪽으로 이동시키는 과정을 반복.

# numbers = [63, 31, 27, 11, 25]
# def bubble(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr) -i -1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#
#
# bubble(numbers)
# print(numbers)

### 카운팅 정렬 : 정수를 정렬하는 알고리즘, 각 숫자의 갯수를 세어서 정렬

# numbers = [1, 2, 4, 2, 3, 1, 2, 4]
# def counting(arr):
#     max_v = max(arr)
#     ##count 리스트에는 몇개있는지 알아야 하므로 가장 큰 숫자보다 하나더(0까지)
#     count_arr = [0] * (max_v +1)
#
#     for num in arr:
#         count_arr[num] += 1
#
#     sorted_list = []
#     for idx, count in enumerate(count_arr):
#         sorted_list.extend([idx] * count)
#
#     return sorted_list
#
# sorted_lst = counting(numbers)
# print(sorted_lst)

### 순열 : 주어진 항목들로 만들 수 있는 모든 가능한 순서(튜플)
### itertools 모듈 사용

# from itertools import permutations
# arr = [1, 2, 3, 4, 5, 6]
# result = list(permutations(arr))
# print(result)

### 탐욕 알고리즘 : 각 단계에서 가장 최선의 선택을 하는 방법
### 거스름돈을 줄 때 가장 적은 수의 동전을 사용하여 거스름돈을 주는 법
# 실습: 동전 종류가 100원, 50원, 10원 거스름돈이 380원이라면
# 어떻게 해야 가장 적은 수의 동전으로 거스름돈을 받을 수 있을까요

# count100 = 0
# count50 = 0
# count10 = 0
# N = int(input())
# while N > 0:
#     count100 += N//100
#     N = N % 100
#     count50 += N//50
#     N = N % 50
#     count10 += N//10
#     N = N % 10
#     if N % 10:
#         break
# print(count100, count50, count10)

# def greedy(money, coins):
#     # 잘못들어와도 거스름돈의 단위 순서로 정렬하기
#     coins.sort(reverse = True)
#     #거스름 돈의 개수를 저장할 딕셔너리
#     change = {coin : 0 for coin in coins}
#     for coin in coins:
#         while money >= coin:
#             money -= coin
#             #해당 coin(동전)의 개수를 1씩 증가
#             change[coin] += 1
#     return change
# result = greedy(380, [100, 10, 50])
# print(result)

#########pb3
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     cards = input()
#     #숫자의 등장 횟수를 저장할 딕셔너리 생성
#     counts = {str(n) : 0 for n in range(10)}
#     #각 숫자의 등장 횟수 세기
#     for card in cards:
#         counts[card] += 1
#     max_count = max(counts.values())
#     # max_count와 같은 횟수를 가진 숫자들 중 가장 큰 숫자를 찾기
#     max_number = max([int(num) for num, count in counts.items() if count == max_count])
#     print(f'#{tc} {max_number} {max_count}')


#### pb4
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr= list(map(int, input().split()))
#     new_arr = []
#
#     for j in range(N - M + 1):
#         result = 0
#         # j부터 j+m까지의 합
#         for k in range(j, j+M):
#             result += arr[k]
#         new_arr.append(result)
#     max_arr = max(new_arr)
#     min_arr = min(new_arr)
#     print(f'#{tc} {max_arr - min_arr}')