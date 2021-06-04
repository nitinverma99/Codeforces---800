for i in range(int(input())):
    k = int(input())
    lst = list(map(int, input().split()))
    if sum(lst)%2 != 0:
        print("YES")
    else:
        odd = 0
        even = 0
        for i in range(len(lst)):
            if lst[i]%2 == 0:
                even += 1
            else:
                odd += 1
        if odd == len(lst) or even == len(lst):
            print("NO")
        else:
            print("YES")