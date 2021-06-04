n = int(input())
lst = list(map(int, input().split()))
one = []
two = []
three = []
if lst.count(1) >= 1 and lst.count(2) >= 1 and lst.count(3) >= 1:
    teams = min([lst.count(1),lst.count(2),lst.count(3)])
    print(teams)

    for i in range(len(lst)):
        if lst[i] == 1:
            one.append(i+1)
        elif lst[i] == 2:
            two.append(i+1)
        else:
            three.append(i+1)
    for i in range(teams):
        print(one[i], two[i], three[i])
else:
    print('0')