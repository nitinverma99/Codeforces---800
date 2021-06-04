for i in range(int(input())):
    x,y,z = list(map(int, input().split()))
    if x==y==z:
        print('YES')
        print(x,y,z, sep=" ")
    else:
        a = 1
        b = x
        c = y
        if z!= max(b,c):
            print('NO')
        else:
            print('YES')
            print(a,b,c, sep=" ")