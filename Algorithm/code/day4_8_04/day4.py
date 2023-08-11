## 부분 집합 원소 찾기
arr = [1, 2, 3]
n = len(arr)
list1 = []
for i in range(1 << n):  #부분집합의 개수
    list2 = []  # j반복이 끝나면 list 2초기화
    for j in range(n): #원소의 수만큼 비트를 비교
        if i & (1 << j):# i의 j번 비트가 1인경우

            list2.append(arr[j]) #j번 원소 출력
    list1.append(list2) #j반복문이 끝나고 난 이후 list1에 추가
## 부분집합의 합이 0인 경우찾기
for i in list1:
    if sum(i) == 0:
        print(f'{i}, {sum(i)}')

## 이진 검색 알고리즘
def binarySearch(a, N, key):
    start = 0
    end = N - 1
    while start <= end: #탐색구간의 존재 원소가 한개 이상
        # strat < end 이렇게 만들면 2개 이상
        middle = (start +end)// 2
        if a[middle] == key:  ##검색 성공
            return True
        elif a[middle] > key:
            end = middle -1
        else:
            start = middle + 1  ##가운데값이 아닐때 좌우 선택후 다시 탐색
    return False ##그래도 없다면 검색 실패
## 재귀함수 이용
## 추후에 더 자세히 배울 예정
def binarySearch2(a, low, high, key):
    if low > high: #검색 실패
        return  False
    else:
        middle = (low + high)//2
        if key == a[middle]:
            return True
        elif key < a[middle]:
            return binarySearch2(a, low, middle-1, key)
        elif key > a[middle]:
            return binarySearch2(a, middle+1, high, key)

##선택정렬
def SelectionSort(arr, n):
    for i in range(n-1):
        minIdx = i
        for j in range(i+1, n):
            #나머지 구간에서 최소값의 위치 찾기
            if arr[minIdx] > arr[j]:
                minIdx = j
        #for문 안에서가 아니라 그 구간에서 최소값을 찾은 이후 자리 바꾸기
        arr[i], arr[minIdx] = arr[minIdx], arr[i]
##k번째로 작은 원소를 찾기(선택 정렬 응용)
def SelectionSort(arr, k):
    for i in range(0, k):
        minIdx = i
        for j in range(i + 1, len(arr)):
            # 나머지 구간에서 최소값의 위치 찾기
            if arr[minIdx] > arr[j]:
                minIdx = j
        # for문 안에서가 아니라 그 구간에서 최소값을 찾은 이후 자리 바꾸기
        arr[i], arr[minIdx] = arr[minIdx], arr[i]

    return arr[k-1]