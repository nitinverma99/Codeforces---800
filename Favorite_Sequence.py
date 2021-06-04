for cases in range(int(input())):
    k = int(input())
    lst = list(map(int, input().split()))
    gst = []
    for i in range(k//2):
        gst.append(lst[i])
        gst.append(lst[k-i-1])
    if k%2 == 0:
        print(*gst)
    else:
        gst.append(lst[k//2])
        print(*gst)