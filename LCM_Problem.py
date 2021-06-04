for cases in range(int(input())):
    l,r = list(map(int, input().split()))
    next = l*2
    if l*2 > r:
        print("-1 -1")
    else:
        print(l, l*2)