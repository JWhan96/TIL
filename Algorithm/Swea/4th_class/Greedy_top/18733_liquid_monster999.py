import heapq
pq = [] # 우선순위 큐
N = int(input())
nums = list(map(int, input().split()))

for num in nums:
    heapq.heappush(pq, num)

sum_v = 0
while len(pq) > 1: #큐에 원소가 1개이상 남아있어야 한다
    a = heapq.heappop(pq) #1 가장작은 값을 꺼낸다
    b = heapq.heappop(pq) #2 그 다음으로 작음 값 꺼내기
    c = a+b
    sum_v += c
    heapq.heappush(pq, c) #더한 값을 다시 우선순위 큐에 넣는다
print(sum_v)