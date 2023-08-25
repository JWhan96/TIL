
# def generate_sublists(lst, num_sublists):
#     if num_sublists == 1:
#         yield [lst]
#         return
#
#     for i in range(1, len(lst)):
#         for sub_list in generate_sublists(lst[i:], num_sublists - 1):
#             yield [lst[:i]] + sub_list
#
# lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# num_sublists = 4
# lst3 = list(generate_sublists(lst1, num_sublists))
#
# for sublist_set in lst3:
#     print(sublist_set)

####
def generate_sublists(lst, num_sublists):
    if num_sublists == 1:
        return [[lst]]

    result = []
    for i in range(1, len(lst)):
        for sub_list in generate_sublists(lst[i:], num_sublists - 1):
            result.append([lst[:i]] + sub_list)

    return result

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num_sublists = 4
lst3 = generate_sublists(lst1, num_sublists)

for sublist_set in lst3:
    print(sublist_set)
