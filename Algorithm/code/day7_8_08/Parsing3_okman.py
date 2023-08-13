'''
입력
____bck____a_c_k_

출력
pass
'''

arr = input()

def Okman(arr):

    result = 0
    oklist = [item for item in arr.split('_') if item != '']  # ['bck', 'a', 'c', 'k']
    unit_list = [item for item in arr if item != '_']  # ['b', 'c', 'k', 'a', 'c', 'k']

    for i in oklist:
        if i == 'bad' or i =='no' or i =='puck':
            result += 1

    for i in range(len(arr) - 5 + 1):
        count = 0
        if arr[i] == '_':
            for k in range(5):
            if count == 5:
                result += 1

    for i in unit_list:
        if i.isdigit():
            result += 1
            break

    for j in unit_list:
        cntresult = unit_list.count(j)
        if cntresult > 5:
            result += 1
            break

    return result
result = Okman(arr)

if result == 0:
    print('pass')
elif result >= 1:
    print('fail')


