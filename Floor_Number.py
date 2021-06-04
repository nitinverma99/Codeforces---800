for cases in range(int(input())):
    n, x= list(map(int, input().split()))
    count = 1
    if n==1 or n==2:
        print('1')
    else:
        lower =  2
        upper = 2+x
        for i in range(2,n):
        
            count += 1
            if lower <= n and upper >= n:
                print(count)
                break
            else:
                lower += x
                upper += x
        