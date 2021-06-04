for cases in range(int(input())):
    x,y,n = list(map(int, input().split()))
    if n<x:
        print(y)
    else:
        remain = n%x
        if remain ==y:
            print(n)
            
        else:
            if remain>y:
                print(n-remain+y)
            else:
                print(n-remain+y-x)