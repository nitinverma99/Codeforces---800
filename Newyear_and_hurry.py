n, k = map(int, input().split())
spare_time = 240 - k
count = 0
for i in range(1, n+1):
    if spare_time - 5*i < 0:
        break
    else:
        spare_time = spare_time - 5*i
        count += 1
print(count)    