for l in range(int(input())):
    k =int(input())
    lst = list(map(int, input().split()))
    for i in range(len(lst)-2):
        if lst[i] == lst[i+1] and lst[i+1] == lst[i+2]:
            continue
        elif lst[i] != lst[i+1] and lst[i+1] == lst[i+2]:
            print(i+1)
            break
        elif lst[i] == lst[i+1] and lst[i+1] != lst[i+2]:
            print(i+3)
            break
        elif lst[i] == lst[i+2] and lst[i] != lst[i+1]:
            print(i+2)
            break