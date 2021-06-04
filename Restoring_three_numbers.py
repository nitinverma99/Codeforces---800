lst = list(map(int, input().split()))
maxx = max(lst)
lst.remove(maxx)
print(maxx - lst[0], maxx - lst[1], maxx - lst[2])