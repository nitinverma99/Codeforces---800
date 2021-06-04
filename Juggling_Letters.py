for cases in range(int(input())):
    k = int(input())
    lst = []
    for m in range(k):
        string = list(input())
        lst = lst + string
    sett = set(lst)
    sett = list(sett)
    for i in range(len(sett)):
        if lst.count(sett[i]) %k == 0:
            if i == len(sett) - 1:
                print("YES")
                break
            continue
        
        else:
            print("NO")
            break