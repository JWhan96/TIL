# key가 있으면 1, 없으면 0을 리턴하는 함수
def f(i, N, key, arr): # i 현재상태, N 목표, key찾고자 하는 원소
    if i == N:
        return 0
    elif arr[i] == key:
        return 1

    else:
        # 0이든 1이든 return이 된다면
        return f(i+1, N, key, arr)

N = 5
arr = [1, 2, 3, 4, 5]
key = 3
print(f(0, N, key, arr))
