n, a, b = list(map(int, input().split()))
minn = min(a,b)
if minn>= n:
    print("Yes")
else:
    print("No")