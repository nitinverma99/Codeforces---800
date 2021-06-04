a1, a2, a3, a4 = list(map(int, input().split()))
lst = list(input())
lst = list(map(int, lst))
count= 0
for i in range(len(lst)):
    if lst[i] == 1:
        count+= a1
    elif lst[i] == 2:
        count+= a2
    elif lst[i] == 3:
        count+= a3
    elif lst[i] == 4:
        count+= a4
print(count)