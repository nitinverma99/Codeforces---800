for i in range(int(input())):
    m,n= list(map(int, input().split()))
    if m == n:
        print('0')
    elif (abs(m-n))%2 == 0 :
        if m>n:
            print('1')
        else:
            print('2')
    else:
        if m>n:
            print('2')
        else:
            print('1')