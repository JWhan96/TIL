def find_max_two(arr):
    d=1
    if len(arr) < 2:
        return arr
    max1, max2 = arr[:2]
    if max2 > max1:
        max1, max2 = max2, max1
    for n in arr[2:]:
        if n > max1:
            max1, max2 = n, max1
        elif n > max2:
            max2 = n
    return [max1, max2]

find_max_two([3, -1, 5, 0, 7, 4, 9, 1])