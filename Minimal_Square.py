n = int(input())
for i in range(n):
    a, b = list(map(int, input().split()))
    if a>b :
        a,b = b,a
    print(max(a*2,b)*max(a*2,b))