n = int(input())
lst = []
for i in range(1,10):
    lst.extend((i, i*11, i*111, i*1111))
for i in range(n):
    inp = int(input())
    index = lst.index(inp)
    gst = lst[0:index+1]
    for i in range(len(gst)):
        gst[i] = str(gst[i])
    total = ''.join(gst)
    print(len(total))