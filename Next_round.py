a, b =  map(int, input().split(' '))
lst = list(map(int, input().split(' ')))
def is_greater(lst):
    k = lst[b-1]
    n = 0
    for i in lst:
        if i == 0:
            continue
        elif i >= k:
            n += 1
    return n 

print(is_greater(lst))
