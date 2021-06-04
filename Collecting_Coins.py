n = int(input())
for i in range(n):
    lst = list(map(int, input().split()))
    brought = lst[-1]
    lst.pop()
    maxx = max(lst)
    if (3*maxx - (lst[0] + lst[1] + lst[2] )) > brought:
        print('NO')
    else:
        remain =brought - ( 3*maxx - (lst[0] + lst[1] + lst[2] ))
        if remain%3 == 0:
            print('YES')
        else:
            print('NO')