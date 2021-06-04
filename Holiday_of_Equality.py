from functools import reduce
n = int(input())
lst = list(map(int, input().split()))
maxx = max(lst)
lst = [(maxx-i) for i in lst]
final = reduce(lambda x,y: x+y, lst)
print(final)
