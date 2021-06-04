n = int(input())
a = list(map(int, input().split()))
a = set(a[1:])
b = list(map(int, input().split()))
b = set(b[1:])
c = a.union(b)
if 0 in c:
    c.remove(0)
if n == len(c):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")