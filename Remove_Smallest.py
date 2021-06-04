n = int(input())
for i in range(n):
    k = int(input())
    lst = list(map(int, input().split()))

    if len(lst) == 1:
        print("YES")
        continue
    
    else:
        lst.sort()
        for i in range(len(lst)-1):
            if (lst[i+1] - lst[i]) <= 1 :
                if i == len(lst)-2 :
                    print("YES")
                    break
                continue
            else:
                print("NO")
                break