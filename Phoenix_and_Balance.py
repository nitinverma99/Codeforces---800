n = int(input())
for i in range(n):
    k = int(input())
    lst = []
    gst = []
    for i in range(k):
        lst.append(2**(i+1))
    for i in range(k//2-1):
        gst.append(lst[i])
    gst.append(lst[k-1])
    extra = sum(lst) - sum(gst)
    final = sum(gst)- extra
    print(final)
