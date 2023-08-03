T = int(input())
for tc in range(1, T+1):
    total, a_goal, b_goal = map(int, input().split())

    def binarySearch(total, goal):
        count = 0
        start = 1
        end = total

        while start <= end:
            #여기 왜이렇게 되는거지
            middle = (start+end)//2
            if middle == goal:
                count += 1
                return count
            elif middle > goal:
                end = middle
                count += 1
            elif middle < goal:
                start = middle
                count += 1
        return count
    acount = binarySearch(total, a_goal)
    bcount = binarySearch(total, b_goal)

    if acount < bcount:
        winner = 'A'
    elif acount == bcount:
        winner = 0
    elif acount > bcount:
        winner = 'B'

    print(f'#{tc} {winner}')