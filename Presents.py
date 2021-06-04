n = int(input())
lst = list(map(int, input().split()))
gst = []
for i in range(1, len(lst)+1):
    indii = lst.index(i)
    gst.append(indii+1)
print(*gst)