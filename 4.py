def recursive_sum(lst):
    return lst[0] + recursive_sum(lst[1:])


print(recursive_sum([1, 2, 3, 4]))  