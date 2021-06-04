for i in range(int(input())):
    n, m = list(map(int, input().split()))
    if n==1 and m==1:
        print('1')
    else:
        multi = n*m
        if multi%2 == 0:
            print(multi//2)
        else:
            print((multi+1)//2)