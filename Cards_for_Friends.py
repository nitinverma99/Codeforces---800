for i in range(int(input())):
    w,h,n = list(map(int, input().split()))
    if w%2 != 0 and h%2 != 0:
        if n == 1:
            print('YES')
        else:
            print('NO')
    else:
        count= 0
        i=1
        while(w%2 == 0 or h%2 ==0 ):
            if h%2 == 0:
                h = h//2
                count = 2**i
                i +=1
            elif w%2 == 0:
                w = w//2
                count = 2**i
                i += 1
            if count >= n:
                print("YES")
                break
            else:
                continue
        if count < n:
            print("NO")
    