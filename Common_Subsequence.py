for cases in range(int(input())):
    n,m= list(map(int, input().split()))
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))
    count = 0
    for i in range(n-1, -1, -1):
        if lst1[i] in lst2:
            count = lst1[i]
            print("YES")
            print("1", count)
            break
        elif i == 0:
            print("NO")
            break
        else:
            continue
   