for i in range(int(input())):
    n, k = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    gst = list(map(int, input().split()))
    while(k>0):
        if max(gst)>min(lst):
            maxx = max(gst)
            minn = min(lst)
            lst.append(maxx)
            lst.remove(minn)
            gst.remove(maxx)
            k -= 1
        else:
            break
    print(sum(lst))