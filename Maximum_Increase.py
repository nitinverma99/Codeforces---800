n= int(input())
lst = list(map(int, input().split()))
maxx = 1
count = 1
for i in range(n-1):
    if lst[i+1] > lst[i]:
        count += 1
    else:
        if count> maxx:
            maxx = count
        count =1
if count > maxx:
    print(count)
else:
    print(maxx)
