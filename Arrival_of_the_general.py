n = int(input())
lst = list(map(int, input().split()))
minn = min(lst)
maxx = max(lst)
count_min = lst.count(minn)
count_max = lst.count(maxx)
index_min = lst.index(minn)
index_max = lst.index(maxx)
for i in range(n):
    if lst[i] == minn :
        index_min = i
for i in range(n-1, -1, -1):
    if lst[i] == maxx:
        index_max = i

if index_max > index_min:
    print(index_max + (n-1-index_min) - 1)
else:
    print(index_max +n -1 - index_min)