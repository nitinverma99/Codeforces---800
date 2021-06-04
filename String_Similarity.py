for cases in range(int(input())):
    k = int(input())
    s = (input())
    gst = []
    for i in range(len(s)-k+1):
        gst.append(s[i:i+k])
    for i in range(len(gst)):
        gst[i] = gst[i][i]
    print(''.join(gst))