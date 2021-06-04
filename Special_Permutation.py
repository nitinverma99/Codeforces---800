for i in range(int(input())):
    k = int(input())
    lst = []
    for i in range(k, 0, -1):
        if i == 1:
            lst.insert(k, 1)
        else:
            lst.insert(0, i)
    print(*lst)        