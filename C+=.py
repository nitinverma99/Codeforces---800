for cases in range(int(input())):
    a,b,n = list(map(int, input().split()))
    count = 0
    while (max(a,b) <= n):
        if a<b:
            a += b
        else:
            b += a
        count += 1
    print(count)