for i in range(int(input())):
    k = int(input())
    lst = list(map(int, input().split()))
    if lst.count(1)%2 != 0:
        print("NO")
    elif lst.count(2)%2 ==0 and lst.count(1)%2 == 0:
        print("YES")
    elif lst.count(2) != 0 and lst.count(1)%2 ==0 and lst.count(1) >= 2:
        print("YES")
    else:
        print("NO")