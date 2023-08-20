## 배열 2(Array 2)
### 목차
- [배열: 2차원 배열](#2차원-배열의-선언)
- [부분집합 생성]()
- [검색 (Search)]()
  - [순차 검색(Sequential Search)]()
  - [바이너리 서치 (Binary Search)]()
- [셀렉션 알고리즘 (Selection algorithm)]()
- [선택 정렬 (Selection Sort)]()

#### 2차원 배열의 선언

- 1차원 List를 묶어놓은 List
- 2차원 이상의 다차원 List는 차원에 따라 Index를 선언
- 2차원 List의 선언: 세로길이(행의 개수), 가로길이(열의 개수)를 필요로 함
- Python 에서는 데이터 초기화를 통해 변수선언과 초기화가 가능

```py
arr = [
    [0, 1, 2, 3],
    [4, 5, 6, 7]    # 2행 4열의 2차원 List
    ]
```
<details>
<summary>배열 생성 참고</summary>

<!-- summary 아래 한칸 공백 두어야함 -->
```
3
1 2 3
4 5 6
7 8 9

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

#결과:
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
        ]
```

</details>


### 2차원 배열의 접근
- 배열 순회
  - n X M 배열의 모든 원소를 빠짐없이 조사하는 방법
- 행 우선 순회   
  ```
  # i 행의 좌표
  # j 열의 좌표

  for i in range(n):
    for j in range(m):
        f(Array[i][j]) # 필요한 연산 수행  
  ```
- 열 우선 순회
  ```
  # i 행의 좌표
  # j 열의 좌표

  for i in range(m):
    for j in range(n):
        f(Array[j][i]) # 필요한 연산 수행 
  ```
- 지그재그 순회
  ```
  # i 행의 좌표
  # j 열의 좌표

  for i in range(n):
    for j in range(m):
        f(Array[i][j + (m-1-2*j) * (i%2)]) # 필요한 연산 수행
  ```
- 델타를 이용한 2차 배열 탐색
  - 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법
  ```
  arr[0...N-1][0...N-1] # N X N 배열
  di[] <- [0, 1, 0, -1]
  dj[] <- [1, 0, -1, 0]
  for i : 0 -> N-1 :
    for j : 0 -> N-1 :
        for k in range(4):
            ni <- j + di[k]
            nj <- j + dj[k]
            if 0 <= ni < N and 0 <= nj < N # 유효한 인덱스면
                f(arr[ni][nj]) 
  ```

#### 2차원 배열의 활용
- 전치행렬
  ```
  # i : 행의 좌표, len(arr)
  # j : 열의 좌표, len(arr[0])
  arr = [
    [1, 2, 3],
    [4, 5, 6,],  # 3*3행렬
    [7, 8, 9]
    ] 

  # arr_T = [list(row) for row in zip(*arr)] 이 방법 이용하면 편리
  for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]  
  # 결과
  [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
    ]           
  ```

### 부분집합 생성하기
- 완전검색 기법을 사용할 경우 집합의 모든 부분집합을 생성해야 한다.
  
<details>
<summary>부분집합의 수</summary>

<!-- summary 아래 한칸 공백 두어야함 -->
- 집합의 원소가 n개일 때, 공집합을 포함한 부분집합의 수는 2^n개이다.
- 이는 각 원소를 부분집합에 포합시키거나 포합시키지 않는 2가지 경우를 모든 원소에 적용한 경우와 같다.
- 예) {1, 2, 3, 4}  => 2 x 2 x 2 x 2 = 16가지

</details>

- 각 원소가 부분집합에 포함되었는지를 for loop를 이용하여 확인하고 부분집합을 생성하는 방법
  ```
  bit = [0, 0, 0, 0]
  for i in range(2):
    bit[0] = i                 # 0번 원소
    for j in range(2):    
      bit[1] = j               # 1번 원소
      for k in range(2):
        bit[2] = k             # 2번 원소
        for l in range(2):
          bit[3] = l           # 3번 원소
          print_subset(bit)    # 생성된 부분집합 출력
  ```


<br> <!-- 빈 줄을 추가하여 간격을 만듭니다 -->

### 비트 연산자
<details>
<summary>비트 연산자</summary>


- & : 비트 단위로 AND 연산
- | : 비트 단위로 OR 연산
- << : 피연산자의 비트 열을 왼쪽으로 이동
- \>> : 피연산자의 비트 열을 오른쪽으로 이동

</details>
<br> <!-- 빈 줄을 추가하여 간격을 만듭니다 -->
- 비트연산자를 이용하여 보다 간결하게 부분집합을 생성하는 방법
  
```
arr = [3, 6, 7, 1, 5, 4]

n = len(arr)                     # n : 원소의 개수

for i in range(1<<n) :           # 1<<n : 부분 집합의 개수
  for j in range(n) :            # 원소의 수만큼 비트를 비교
    if i & (1<<j) :              # i의 j번 비트가 1인경우
      print(arr[j], end = ', ')  # j번 원소 출력
  print()
print() 

```
#### 예시
```
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
```

