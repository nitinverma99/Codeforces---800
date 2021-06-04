n = int(input())
lst = list(map(int, input().split()))
count = 0
best = lst[0]
worst = lst[0]
for i in range(1, n):
    if lst[i] > best :
        count +=1
        best = lst[i]
    elif lst[i] < worst:
        count += 1
        worst = lst[i]
    else:
        continue
print(count)