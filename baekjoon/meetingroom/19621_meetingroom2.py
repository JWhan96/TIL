N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0

arr.sort(key = lambda x: x[0])
arr.sort(key = lambda x: x[1])

for i in range(N):

    index = 0 ###임의의 회의 K(1≤ K ≤ N)는 회의 K − 1과 회의 K + 1과
              ###회의시간이 겹치고 다른 것과는 겹치지 않으므로 1로 초기화
    for k in range(N-i): ## ex) 135 146 등 모든 경우의 수를 위함
        people = 0
        curr = arr[i][1] #끝나는 시간
        index += 1
        people += arr[i][2]
        for j in range(i+index, N):

            if arr[j][0] >= curr: #다음 시작시간이 끝나는 시간보다 크거나 같을 때
                people += arr[j][2]
                curr = arr[j][1] #다음끝나는 시간을 조건 맞았을때 종료시간으로 변경
                continue
        result = max(people, result)

print(result)

