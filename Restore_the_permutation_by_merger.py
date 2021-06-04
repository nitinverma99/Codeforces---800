n = int(input())
for i in range(n):
    k = int(input())
    lst= list(map(int, input().split()))
    gst = []
    for i in range(len(lst)):
        if lst[i] not in gst:
            gst.append(lst[i])
        else:
            continue
    print(*gst, sep=" ")