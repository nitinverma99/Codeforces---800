k, r = map(int, input().split())
count=0
for i in range(1, 10):
    if (k*i) % 10 == 0:
        count = i
        break
    elif (k*i) % 10 == r:
        count= i
        break
print(count)