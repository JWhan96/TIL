## 재귀함수 1. 자기자신호출 2. 종료조건 반드시 포함
## f1=1, f2=3, f3=5, f4=11, f5=21, f6= 43, f7=85
## 피보나치 수열처럼 접근
T = int(input())
for tc in range(1, T+1):
    N = int(input())

    def paper(n):
        if n == 10:
            return 1
        if n == 20:
            return 3
        else:
            return paper(n-10) + 2 * paper(n-20)

    print(paper(N))
