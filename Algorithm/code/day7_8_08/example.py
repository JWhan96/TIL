String = input()
N = len(String)
def ddd(N, String):
    d=1
    split = [0] * N
    for i in range(N):
        try:
            int(String[i])
        except ValueError:
            split[i] = 1
    split.append(1)
    print(split)
    peoples = 1
    for i in range(N):
        if split[i] + 1 == split[i+1]:
            peoples += 1

    pos = 0
    for i in range(peoples):
        name = ''
        num = 0
        for j in range(pos, N):
            if split[j] + 1 == split[j+1]:
                num = num*10 + int(String[j]) + 17
                pos = j + 1
                print(f'{name}#{num}')
                break
            if split[j] == 1:
                name += String[j]
            if split[j] == 0:
                num = num*10 + int(String[j])
ddd(N, String)

