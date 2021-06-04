for cases in range(int(input())):
    n,d = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    minn1 = min(lst)
    lst.remove(minn1)
    minn2 = min(lst)
    count = 0
    for i in range(len(lst)):
        if lst[i] > d:
            count += 1
        else:
            continue
    if count == 0 :
        print("YES")
    else: 
        if (minn1 + minn2) <= d:
            print("YES")
        else:
            print("NO")
