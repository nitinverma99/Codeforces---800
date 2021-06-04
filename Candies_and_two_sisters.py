n = int(input())
for i in range(n):
    k = int(input())
    if k == 1:
        print('0')
    elif k == 2:
        print('0')
    else:
        if k%2 == 0:
            print(k//2 - 1)
        else:
            print((k-1)//2)