# 그래프 & 백트래킹
## 목차
- [그래프 기본]
- [DFS]
- [BFS]
- [서로소 집합들]
- [최소 비용 신장트리(MST)]
- [최단 경로]

### 그래프
- 그래프는 아이템(사물 또는 추상적 개념)들과 이들 사이의 연결 관계를 표현
- 그래프는 정점(Vertex)들의 집합과 이들을 연결하는 간선(Edge)들의 집합으로 구성된 자료구조
  - |V|: 정점의 개수
  - |E|: 그래프의 포함된 간선의 개수
  - |V|개의 정점을 가지는 그래프는 최대 |V|(|V|-1)/2 간선이 가능
  - ex) 5개 정점이 있는 그래프의 최대 간선 수는 10(=5*4/2)개
- 선형 자료구조나 트리 자료구조로 표현하기 어려운 N:N 관계를 가지는 원소들을 표현하기에 용이

#### 그래프 유형
- 무향 그래프(Undirected Graph)
- 유향 그래프(Directed Graph)
- 가중치 그래프(Weighted Graph)
- 사이클 없는 방향 그래프(DAG, Directed Acyclic Graph)
- 완전 그래프
  - 정점들에 대해 가능한 모든 간선들을 가진 그래프
- 부분 그래프
  - 원래 그래프에서 일부의 정점이나 간선을 제외한 그래프



### 그래프 표현
- 간선의 정보를 저장하는 방식, 메모리나 성능을 고려하여 결정
- 인접 행렬(Adjacent matrix)
  - |V| x |V|크기의 2차원 배열을 이용해서 간선 정보를 저장
  - 배열의 배열(포인터 배열)
- 인접 리스트(Adjacent List)
  - 각 정점마다 해당 정점으로 나가는 간선의 정보를 저장
- 간선의 배열
  - 간선(시작 정점, 끝 정점)을 배열에 연속적으로 저장

### 인접 행렬
장점: 구현이 쉽다, 단점: 메모리 낭비가 심하다(0까지 표현)
- 두 정점을 연결하는 간선의 유무를 행렬로 표현




#### DFS
- stack 버전
  ```py
  def dfs_stack(start):
      visited = []
      stack = [start]
      while stack:
          now = stack.pop()
          # 이미 방문한 지점이라면 continue
          if now in visited:
              continue
          # 방문하지 않은 지점이라면 방문 표시
          visited.append(now)
          # 갈 수 있는 곳들을 stack에 추가
          # for next in range(5):   #dfs stack = 0 3 4 1 2
          for next in range(4, -1, -1): # dfs stack = 0 1 2 3 4
              # 연결이 안되어 있다면 continue
              if graph[now][next] == 0:
                  continue
              # 방문한 지점이라면 stack에 추가하지 않음
              if next in visited:
                  continue

              stack.append(next)
      # 출력을 위한 반환
      return visited

  graph = [[0, 1, 0, 1, 0],
          [1, 0, 1, 1, 1],
          [0, 1, 0, 0, 0],
          [1, 1, 0, 0, 1],
          [0, 1, 0, 1, 0]]
  print(f'dfs stack =', *dfs_stack(0))
  ```
- 재귀 버전
  - map 크기(길이)를 알 때 append형식 말고 재귀 방식을 사용하면 훨씬 빠르다.
  ```py
  visited = [0] * 5
  path = [] #방문 순서 기록
  
  def dfs(now):
      visited[now] = 1 #현재 지점 방문 표시
      print(now, end=" ")
      path.append(now)
      #인접한 노드들을 방문
      for next in range(5):
          if graph[now][next] == 0:
              continue
  
          if visited[next]:
              continue
  
          dfs(next)
  
  graph = [[0, 1, 0, 1, 0],
          [1, 0, 1, 1, 1],
          [0, 1, 0, 0, 0],
          [1, 1, 0, 0, 1],
          [0, 1, 0, 1, 0]]
  print(f'dfs 재귀 =', end = ' ')
  dfs(0)
  print(*path)
  ```


#### BFS
  ```py
  def bfs(start):
      visited = [0] * 5
      # 먼저 방문한 요소들을 먼저 처리
      queue = [start]
      visited[start] = 1
  
      while queue:
          # queue의 맨 앞 요소를 꺼냄
          now = queue.pop(0)
          print(now, end = ' ')
  
          #인접한 노드들을 queue에 추가
          for next in range(5):
              #연결이 안되어 있다면 continue
              if graph[now][next] == 0:
                  continue
              # 방문한 지점이라면 queue에 추가 x
              if visited[next]:
                  continue
  
              queue.append(next)
              #bfs여서 여기서 방문 표시를 해도 무관
              visited[next] =1
  
  
  
  graph = [[0, 1, 0, 1, 0],
           [1, 0, 1, 1, 1],
           [0, 1, 0, 0, 0],
           [1, 1, 0, 0, 1],
           [0, 1, 0, 1, 0]]
  print('bfs 인접행렬 queue =', end=' ')
  bfs(0)
  ```



### 인접 리스트
- 갈 수 있는 지점만 저장
- 메모리가 인접 행렬에 비해 훨씬 효율적
- 주의사항
  - 각 노드마다 갈 수 있는 지점의 개수가 다름
  - range쓸 때 index 조심
#### DFS  
- stack 사용
  ```py
  def dfs_stack(start):
      visited = []
      stack = [start]
      while stack:
          now = stack.pop()
          # 이미 방문한 지점이라면 continue
          if now in visited:
              continue
          # 방문하지 않은 지점이라면 방문 표시
          visited.append(now)
  
          for to in range(len(graph[now])-1, -1, -1):
              # 연결이 안되어 있다면 continue
              # 연결이 되어있는 부분만 저장했으므로 체크할 필요없음
              # if graph[now][next] == 0:
              #     continue
              next = graph[now][to]
              # 방문한 지점이라면 stack에 추가하지 않음
              if next in visited:
                  continue
  
              stack.append(next)
      # 출력을 위한 반환
      return visited
  graph = [
      [1, 3],
      [0, 2, 3, 4],
      [1],
      [0, 1, 4],
      [1, 3]
  ]
  print(f'dfs stack =', *dfs_stack(0))
  ```




### 서로소 집합(Disjoint-sets)
- 서로소 또는 상호배타 집합: 서로 중복 포함된 원소가 없는 집합
  - 교집합 존재 X
- 집합에 속한 하나의 특정 멤버를 통해 각 집합들을 구분
  - 이를 대표자(representative)라고 칭함
- 상호배타 집합 표현 방법
  - 연결 리스트
  - 트리
- 상호배타 집합 연산
  - Make-Set(x)
    - 각 요소들 만들기
  - Find-Set(x) 
    - 각 요소가 내가 속한 그룹의 대표자를 어떻게 찾을지
  - Union(x, y) 
    - 대표자 저장(같은 그룹으로 묶기)   
  - ![서로소 집합](img/서로소%20집합.PNG)





```py
# 0 ~ 9
# make set - 집합을 만들어 주는 과정
# 각 요소가 가리키는 값이 부모
parent = [i for i in range(10)]

# find-set
# x를 기준을로 부모를 찾아가는 함수
def find_set(x):
    if parent[x] == x:
        return x
    # if parent[x] != x:
    #    find_set(parent[x])
    return find_set(parent[x])
    
    '''
    Path compression???
    경로압축
    parent[x] = find_set(parent[x])
    return parent[x]
    
    size와 height(rank?)둘중에 작은 것을 합치는거 내용 구글링 
    '''
# union
# 같은 집합으로 묶어주는 함수
def union(x, y):
    # 1. 이미 같은 집합인지 체크
    x = find_set(x)
    y = find_set(y)
    # 대표자가 같으니, 같은 집합이다.
    if x == y:
        print('싸이클 발생')
        return

    # 2. 다른 집합이라면, 같은 대표자로 수정
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
union(0, 1)
union(2, 3)
union(1, 3)
# union(0, 2) # 추가하게 되면 싸이클 발생(모든 요소가 연결되었으므로)

# 대표자 검색
print(find_set(2))
print(find_set(1))

# 같은 그룹인지 판별
t_x = 0
t_y = 2

if find_set(t_x) == find_set(t_y):
    print(f'{t_x} 와 {t_y} 는 같은 집합에 속해 있다.')
else:
    print(f'{t_x} 와 {t_y} 는 같은 집합에 속해 있지 않다.')

```