def recursive_sum(lst):
    if len(lst) == 0: # if list is empty 
        return 0
    return lst[0] + recursive_sum(lst[1:]) # first element + other element => X+(X+1...)

print(recursive_sum([1, 2, 3, 4])) # result : 10