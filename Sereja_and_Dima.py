n = int(input())
lst = list(map(int, input().split()))
sereja = 0
dima = 0
i = 0
while(len(lst)>0):
    if i%2 == 0:
        if lst[0] > lst[len(lst) - 1]:
            sereja += lst[0]
            lst.pop(0)
            i += 1
        else:
            sereja += lst[len(lst)-1]
            lst.pop(len(lst)-1)
            i+=1
    else:
        if lst[0] > lst[len(lst) - 1]:
            dima += lst[0]
            lst.pop(0)
            i += 1
        else:
            dima += lst[len(lst)-1]
            lst.pop(len(lst)-1)
            i+=1
print(sereja, dima)