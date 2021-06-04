n  = int(input())
for i in range(n):
    k = int(input())
    lst = list(map(int, input().split()))
    gst = []
    lst.sort()
    for i in range(k-1):
        gst.append(lst[i+1]- lst[i])
    print(min(gst))