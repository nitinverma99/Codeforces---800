n = int(input())
lst = []
count = 0
for i in range(n):
    a, b = map(int, input().split())
    lst.append((a,b))
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        else:
            if lst[i][1] == lst[j][0]:
                count += 1
print(count)