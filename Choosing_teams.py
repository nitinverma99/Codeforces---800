n, k = map(int, input().split())
lst = list(map(int, input().split()))
count = 0
lst = [(5-i) for i in lst]
gst = []
for i in range(len(lst)):
    if lst[i] >= k:
        gst.append(lst[i])
print(len(gst)//3)