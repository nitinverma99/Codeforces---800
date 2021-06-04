n, fence_height = map(int, input().split())
lst = list(map(int, input().split()))
count = 0
for i in lst:
    if i > fence_height:
        count += 2 
    else:
        count += 1
print(count)